import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from decorators.retry import retry
from config.settings import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD

class Email:
    def __init__(self, subject, body, recipients, attachments=None):
        self.subject = subject
        self.body = body
        self.recipients = recipients
        self.attachments = attachments or []

    def format_email(self):
        msg = MIMEMultipart()
        msg["Subject"] = self.subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(self.recipients)

        msg.attach(MIMEText(self.body, "plain"))

        for path in self.attachments:
            with open(path, "rb") as file:
                part = MIMEApplication(file.read(), Name=os.path.basename(path))
                part["Content-Disposition"] = f'attachment; filename="{os.path.basename(path)}"'
                msg.attach(part)

        return msg

    @retry(max_attempts=3)
    def send(self):
        msg = self.format_email()

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, self.recipients, msg.as_string())
            print("Email sent successfully.")
