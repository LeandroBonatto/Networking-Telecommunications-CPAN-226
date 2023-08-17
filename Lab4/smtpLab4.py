# import smtp libraby
import smtplib
# security layer
import ssl
import base64
# installing library
from email.message import EmailMessage
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# email created for testing
email_sender = 'l01281271@gmail.com'
# 16 character password generate by google
email_password = 'kvinzfinnwravyqg'
# set receiver
email_receiver = 'bonattoleandro@gmail.com'
# set cc recipients
cc_recipients = ['networkingtest@gmail.com', 'testnetworking@gmail.com']
# set attachment path
attachment_path = 'lab4test.docx'

subject = 'Python SMTP email'
body = """ Testing... """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Cc'] = ', '.join(cc_recipients)
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, [email_receiver] + cc_recipients, em.as_string())
  smtp.quit()
