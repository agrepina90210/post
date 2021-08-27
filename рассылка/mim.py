import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pict


def post(from_email,password,to_email,subject,body,postcard,post_host):
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] =from_email

    body = MIMEText(body)
    message.attach(body)

    with open(postcard, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        'Content-Disposition',f'attachment; filename= {postcard}')
    message.attach(part)

    text = message.as_string()
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(f'smtp.{post_host}', 465, context=context) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, text)


