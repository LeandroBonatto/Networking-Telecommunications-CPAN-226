import smtplib
import ssl
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from django.shortcuts import render

def join_emails(emails):
    if len(emails) > 1:
        return ', '.join(emails)  # join with comma the positions of the list
    else:
        return emails[0]

def send_email(sender_email, sender_password, recipient_emails, cc_email, subject, body, attachment):
    em = MIMEMultipart()
    em['From'] = sender_email
    em['To'] = join_emails(recipient_emails)
    em['Cc'] = join_emails(cc_email)
    em['Subject'] = subject
    em.attach(MIMEText(body))

    if attachment:
        attachment_name = attachment.name
        attachment_content = attachment.read()

        part = MIMEApplication(attachment_content, Name=basename(attachment_name))
        part['Content-Disposition'] = f'attachment; filename="{basename(attachment_name)}"'
        em.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_emails + [cc_email], em.as_string())

def send_email_view(request):
    if request.method == 'POST':
        # Retrieve form inputs from the POST request
        email_sender = request.POST.get('sender_email')
        email_password = request.POST.get('sender_password')
        email_receiver = request.POST.getlist('receiver_emails')
        cc = request.POST.getlist('cc_email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        attachment = request.FILES.get('attachment')

        # Send the email
        send_email(email_sender, email_password, email_receiver, cc, subject, body, attachment)

    return render(request, 'email_form.html')
