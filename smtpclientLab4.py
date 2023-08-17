import smtplib
import ssl
import base64
from email.message import EmailMessage
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

email_sender = 'sender email address'
email_password = 'sender password'
email_receiver = 'receiver email address'

subject = 'Text message'
body = """  This is a test email implementing smtp protocol """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, em.as_string())
  smtp.quit()

