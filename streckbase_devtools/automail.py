import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient: str, subject:str, body:str):
    load_dotenv('streckbase\.env')
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

def send_mass_email(recipients: str, subject:str, html_template:str, personal_infos: list[tuple], constant_info: list[tuple]):
    """
    Loops over 'recipient' and 'personal infos' and sends personalized emails to all adresses in 'recipient'
    
    Unpacks 'personal_infos' followed by 'constant_info' into the html code

    Make sure there are the same number of substitutions in the html code as in 'personal_infos' and 'constant_info' combined
    """
    for recipient, personal_info in zip(recipients, personal_infos):
        send_email(recipient, subject, html_template.format(*personal_info, *constant_info))
