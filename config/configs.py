
def write_msg(session_data, lead_data):
    msg = {
        "from": "onboarding@resend.dev",
        "to": "myinside74@gmail.com",
        "subject": "AI-Assistant - New Request",
        "html": f"""
        <p>Ciao <strong>Amr</strong>,</p>
        <p>Hai ricevuto una nuova richiesta dal tuo <strong>AI Assistant</strong></p>

        <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
            
            <!-- Sezione Persona -->
            <tr style="background-color:#f2f2f2;">
                <td colspan="2"><strong>I Dettagli Della Persona</strong></td>
            </tr>
            <tr><td><strong>Nome</strong></td><td>{lead_data["name"]}</td></tr>
            <tr><td><strong>Azienda</strong></td><td>{lead_data["company"]}</td></tr>
            <tr><td><strong>Ruolo</strong></td><td>{lead_data["role"]}</td></tr>
            <tr><td><strong>Telefono</strong></td><td>{lead_data["telefone"]}</td></tr>

            <!-- Sezione Richiesta -->
            <tr style="background-color:#f2f2f2;">
                <td colspan="2"><strong>I Dettagli Della Richiesta</strong></td>
            </tr>
            <tr><td><strong>Area</strong></td><td>{session_data["entry_flow"]}</td></tr>
            <tr><td><strong>Situazione</strong></td><td>{session_data["case_type"]}</td></tr>
            <tr><td><strong>Stato</strong></td><td>{session_data["scope"]}</td></tr>

            <!-- Note -->
            <tr style="background-color:#f2f2f2;">
                <td colspan="2"><strong>Note sintetiche</strong></td>
            </tr>
            <tr>
                <td colspan="2">{lead_data["summary_notes"]}</td>
            </tr>

            <!-- Altri dettagli -->
            <tr style="background-color:#f2f2f2;">
                <td colspan="2"><strong>Altri Dettagli</strong></td>
            </tr>
            <tr><td><strong>Ruolo</strong></td><td>{session_data["role"]}</td></tr>
            <tr><td><strong>Urgenza</strong></td><td>{session_data["urgency"]}</td></tr>
            <tr><td><strong>Area</strong></td><td>{session_data["geographic_area"]}</td></tr>

        </table>

        <p>Un saluto,</p>
        <strong>Il Tuo Sincero AI Assistant</strong>
        """
    }
    return msg