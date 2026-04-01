import psycopg2
from datetime import datetime, timezone


class PG_DB:
    def __init__(self, host, port, database, user, password):
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        conn.autocommit = True
        self.cursor = conn.cursor()

        # Sessions table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                entry_flow TEXT,
                case_type TEXT,
                scope TEXT,
                role TEXT,
                urgency TEXT,
                geographic_area TEXT,
                metadata TEXT,
                started_at TIMESTAMP,
                updated_at TIMESTAMP
            )
        """)

        # Leads table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id SERIAL PRIMARY KEY,
                session_id TEXT REFERENCES sessions(id) ON DELETE SET NULL,
                name TEXT,
                company TEXT,
                role TEXT,
                email TEXT,
                telefone TEXT,
                summary_notes TEXT,
                created_at TIMESTAMP
            )
        """)


    # Sessions
    def create_session(self, session_id):
        self.cursor.execute("""
            INSERT INTO sessions (
                id, entry_flow, case_type, scope, role, urgency,
                geographic_area, metadata, started_at, updated_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            session_id,
            None,      # entry_flow
            None,      # case_type
            None,      # scope
            None,      # role
            None,      # urgency
            None,      # geographic_area
            None,      # metadata
            datetime.now(timezone.utc),  # started_at
            datetime.now(timezone.utc)   # updated_at
        ))

    def update_session(self, session_id, data):
        set_clause = ", ".join([f"{key}=%s" for key in data.keys()])
        self.cursor.execute(
            f"""
            UPDATE sessions
            SET {set_clause}, updated_at=%s
            WHERE id=%s
            """,
            [*data.values(), datetime.now(timezone.utc), session_id]
        )

    def get_session(self, session_id):
        self.cursor.execute(
            "SELECT * FROM sessions WHERE id=%s",
            (session_id,)
        )
        row = self.cursor.fetchone()

        if not row:
            return None

        columns = [desc[0] for desc in self.cursor.description]
        result = dict(zip(columns, row))

        # Remove internal fields
        result.pop("id", None)
        result.pop("updated_at", None)

        return result


    # Leads
    def create_lead(self, session_id, data):
        self.cursor.execute("""
            INSERT INTO leads (
                session_id, name, company, role, email,
                telefone, summary_notes, created_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            session_id,
            data.get("name"),
            data.get("company"),
            data.get("role"),
            data.get("email"),
            data.get("telefone"),
            data.get("summary_notes"),
            datetime.now(timezone.utc)
        ))