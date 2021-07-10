#!/usr/bin/env python3

import os
from email.message import EmailMessage
import mimetypes
import smtplib
from dotenv import load_dotenv
import datetime
import getpass

"""Test python email functionality"""

def main():
    source = os.path.join(os.path.expanduser("~"), "data") #USer home plus path
   #source os.path.abspath(os.path.join(os.sep, "data", "input")) #absolute path linux beginning with root
    attachement_path=(os.path.join(source, "exmple.png"))
    #print(attachement_path) #Debug Print
    mime_type, _ =mimetypes.guess_type(attachement_path)
    #print(mime_type) #Debug Print
    mime_type, mime_subtype = mime_type.split('/', 1)
    #user='falk_der_fiese'
    load_dotenv()
    server = os.getenv("SMTP_SERVER")
    port = os.getenv("SMTP_PORT")
    user = os.getenv("SMTP_USER")
    #mail_pass = getpass.getpass('Password? ')
    mail_pass  = os.getenv("SMTP_PASS")
    sender  = os.getenv("SMTP_SENDER")
    recipient  = os.getenv("SMTP_RECP")
    body = """Hey there!
    ...
    ... I'm learning to send emails using Python!"""
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Greetings from {} to {}! At {}'.format(sender, recipient, datetime.datetime.now().strftime("%B %d, %Y - %H:%M:%S"))
    message.set_content(body)
    with open(attachement_path, 'rb') as ap:
        message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachement_path))
    #print(message) #Debug Print
    SMTP_SERVER = "smtp.mail.yahoo.com"
    SMTP_PORT = 587
    mail_server =  smtplib.SMTP(server, port)
    mail_server.set_debuglevel(1)
    mail_server.starttls()
    mail_server.login(user, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()

if __name__ == "__main__":
    main()