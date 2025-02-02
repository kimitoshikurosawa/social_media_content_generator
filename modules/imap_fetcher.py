# modules/imap_fetcher.py
import imaplib
import email
from config import EMAIL_USER, EMAIL_PASSWORD, IMAP_SERVER, IMAP_PORT

def get_emails_from_imap():
    """Récupère les emails depuis la boîte de réception Gmail."""
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL_USER, EMAIL_PASSWORD)
        mail.select("inbox")
        # Vous pouvez adapter la recherche pour filtrer par expéditeur ou par sujet
        status, data = mail.search(None, "ALL")
        emails = []
        if data[0]:
            for num in data[0].split():
                status, msg_data = mail.fetch(num, "(RFC822)")
                msg = email.message_from_bytes(msg_data[0][1])
                emails.append(msg)
        mail.logout()
        return emails
    except Exception as e:
        print("Erreur lors de la récupération des emails :", e)
        return []

def parse_email(msg):
    """Extrait le sujet et le corps (texte brut) d'un email."""
    subject = msg.get("Subject", "")
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                charset = part.get_content_charset() or "utf-8"
                body = part.get_payload(decode=True).decode(charset, errors="ignore")
                break
    else:
        charset = msg.get_content_charset() or "utf-8"
        body = msg.get_payload(decode=True).decode(charset, errors="ignore")
    return subject, body
