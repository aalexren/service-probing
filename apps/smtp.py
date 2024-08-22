import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .generic import EmailClient


class SMTPClient(EmailClient):
    def __init__(self, host: str, port: int, **extra):
        self._host = host
        self._port = port
        self._extra = extra

    def send_email(
        self,
        from_email: str,
        to_email: str,
        subject: str,
        message: str,
        login: str | None = None,
        password: str | None = None,
    ):
        body = self._bootstrap_email_body(from_email, to_email, subject, message)
        try:
            with smtplib.SMTP(self._host, self._port, **self._extra) as smtp:
                if login and password:
                    smtp.starttls()
                    smtp.login(login, password)
                smtp.sendmail(from_email, to_email, body.as_string())
        except smtplib.SMTPConnectError:
            print("Couldn't connect to SMTP server!")
        except smtplib.SMTPException as e:
            print(f"Couldn't send email: {e}")
        except TimeoutError:
            print("The SMTP connection could not be established due to expired timeout!")

    def _bootstrap_email_body(
        self, from_email: str, to_email: str, subject: str, message: str
    ) -> MIMEMultipart:
        body = MIMEMultipart()
        body["From"] = from_email
        body["To"] = to_email
        body["Subject"] = subject
        body.attach(MIMEText(message, "plain", "utf-8"))
        return body
