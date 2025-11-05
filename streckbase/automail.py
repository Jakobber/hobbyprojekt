import os
from dotenv import load_dotenv
load_dotenv('streckbase\.env')
import resend

resend.api_key = os.getenv('RESEND_API')

def send_email(recipient: str, subject: str, html: str):
    resend.Emails.send({
    "from": os.getenv('RESEND_AUTHOR'),
    "replyTo": os.getenv('RESEND_REPLY'),
    "to": recipient,
    "subject": subject,
    "html": html
    })

def send_mass_email(recipients: str, subject:str, html_template:str, personal_infos):
    for recipient, personal_info in zip(recipients, personal_infos):
        html = html_template.format(*personal_info)
        send_email(recipient, subject, html)
