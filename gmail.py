import imaplib
import email
import re

def recuperer_code(imap_server, email_utilisateur, mot_de_passe_app, dossier="INBOX"):
    # Connexion au serveur IMAP
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_utilisateur, mot_de_passe_app)
    mail.select(dossier)

    # Cherche les mails récents
    typ, data = mail.search(None, "ALL")
    mail_ids = data[0].split()
    dernier_mail_id = mail_ids[-1]

    typ, msg_data = mail.fetch(dernier_mail_id, "(RFC822)")
    message = email.message_from_bytes(msg_data[0][1])

    # Récupération du corps du message
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = message.get_payload(decode=True).decode()

    # Extraction du code (exemple : 6 chiffres)
    code_match = re.search(r"\b\d{6}\b", body)
    if code_match:
        return code_match.group()
    else:
        return None