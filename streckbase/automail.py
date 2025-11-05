import os
from dotenv import load_dotenv
load_dotenv('streckbase\.env')
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient, subject, body):
    EMAIL_ADDRESS = os.getenv('EMAIL_ADRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD') 
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print("Error sending email:", e)

def send_mass_email(recipients: str, subject:str, html_template:str, personal_infos, other_info):
    for recipient, personal_info in zip(recipients, personal_infos):
        send_email(recipient, subject, html_template.format(*personal_info, *other_info))
