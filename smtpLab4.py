import smtplib
import ssl
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


def join_emails(emails):
    if len(emails) > 1:
        return ', '.join(emails)  # join with comma the positions of the list
    else:
        return emails[0]


def send_email(sender_email, sender_password, recipient_emails, cc_email, subject, body, attachment_path):
    em = MIMEMultipart()
    em['From'] = sender_email
    em['To'] = join_emails(recipient_emails)
    em['Cc'] = join_emails(cc_email)
    em['Subject'] = subject
    em.attach(MIMEText(body))

    with open(attachment_path, "rb") as fil:
        part = MIMEApplication(fil.read(), Name=basename(attachment_path))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(attachment_path)
        em.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_emails + [cc_email], em.as_string())

# Inputs for the email
email_sender = 'jadev.test.prog@gmail.com'
email_password = 'ezywggsysesoizsb'
email_receiver = ['josearango1202@gmail.com', 'jadev.test.prog@gmail.com']
cc = 'ingjdaj@gmail.com'
subject = 'SMTP Test with CC'
body = """This is a test email implementing the SMTP protocol"""
attachment_path = 'attach.txt'

# Send the email
send_email(email_sender, email_password, email_receiver, cc, subject, body, attachment_path)
