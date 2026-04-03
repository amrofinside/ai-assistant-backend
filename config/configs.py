
def write_msg(session_data, lead_data):
    msg = {
        "from": "onboarding@resend.dev",
        "to": "myinside74@gmail.com",
        "subject": "AI-Assistant - New Request",
        "html": f"""
        <p>Ciao <strong>Amr</strong>,</p>
        <p>Hai ricevuto una nuova richiesta dal tuo <strong>AI Assistant</strong></p>

        <h3>I Dettagli Della Persona:</h3>
        <table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse;">
            <tr><td><strong>Nome</strong></td><td>{lead_data["name"]}</td></tr>
            <tr><td><strong>Azienda</strong></td><td>{lead_data["company"]}</td></tr>
            <tr><td><strong>Ruolo</strong></td><td>{lead_data["role"]}</td></tr>
            <tr><td><strong>Telefono</strong></td><td>{lead_data["telefone"]}</td></tr>
        </table>

        <h3>I Dettagli Della Richiesta:</h3>
        <table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse;">
            <tr><td><strong>Area</strong></td><td>{session_data["entry_flow"]}</td></tr>
            <tr><td><strong>Situazione</strong></td><td>{session_data["case_type"]}</td></tr>
            <tr><td><strong>Stato</strong></td><td>{session_data["scope"]}</td></tr>
        </table>

        <h3>Note sintetiche:</h3>
        <p>{lead_data["summary_notes"]}</p>

        <h3>Altri Dettagli:</h3>
        <table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse;">
            <tr><td><strong>Ruolo</strong></td><td>{session_data["role"]}</td></tr>
            <tr><td><strong>Urgenza</strong></td><td>{session_data["urgency"]}</td></tr>
            <tr><td><strong>Area</strong></td><td>{session_data["geographic_area"]}</td></tr>
        </table>

        <p>Un saluto,</p>
        <strong>Il Tuo Sincero AI Assistant</strong>
        """
    }
    return msg