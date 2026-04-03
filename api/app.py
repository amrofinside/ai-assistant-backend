import uuid
import logging
import resend
from db.dp import PG_DB
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.secrets import postgres_db_url, resend_api_key
from config.configs import write_msg

# Initialize
pgdb = PG_DB(postgres_db_url)
app = FastAPI()
resend.api_key = resend_api_key

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (To be replaced "*" with your frontend URL in production for security)
    allow_credentials=True,
    allow_methods=["*"],  # This allows the OPTIONS method as well
    allow_headers=["*"],
)

# Models
class SessionUpdateRequest(BaseModel):
    session_id: str
    data: dict

class LeadRequest(BaseModel):
    session_id: str
    data: dict

# Logging
logging.basicConfig(level=logging.INFO)

# Endpoints
@app.get("/health")
def health_check():
    logging.info("Health checked: ok")
    return {
        "status": "ok",
        "service": "inside-mvp-backend"
    }


@app.post("/session/start")
def start_session():
    session_id = str(uuid.uuid4())

    pgdb.create_session(session_id)
    logging.info(f"Session created: {session_id}")

    return {
        "session_id": session_id
    }


@app.post("/session/update")
def update_session_endpoint(req: SessionUpdateRequest):
    existing = pgdb.get_session(req.session_id)

    if not existing:
        raise HTTPException(status_code=404, detail="Session not found")

    pgdb.update_session(req.session_id, req.data)
    logging.info(f"Session update: {req.session_id}")

    return {
        "status": "updated"
    }


@app.get("/session/{session_id}")
def get_session_endpoint(session_id: str):
    session = pgdb.get_session(session_id)

    if not session:
        logging.info("Get session ID: Session not found")
        raise HTTPException(status_code=404, detail="Session not found")
    
    logging.info(f"Get session: {session_id}")

    return session


@app.post("/lead")
def submit_lead(req: LeadRequest):
    session = pgdb.get_session(req.session_id)

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Insert the lead into the leads table
    pgdb.create_lead(req.session_id, req.data)
    logging.info(f"A lead saved")

    # Send messasge
    msg_to_send = write_msg(session, req.data)
    email = resend.Emails.send(msg_to_send)
    email_id = email.get("id")
    if not email_id:
        logging.error(f"Failed to send email: {email}")
    else:
        email_data = resend.Emails.get(email_id)
        email_status = email_data.get("last_event")
        logging.info(f"Email {email_id} status: {status}")

    return {
        "status": "success",
        "email_status": email_status
    }