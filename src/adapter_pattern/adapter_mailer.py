import csv
import smtplib
from email.mime.text import MIMEText


class Mailer:
    def send(self, sender, recipients, subject, message):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = [recipients]  # posible error

        s = smtplib.SMTP("locahost")
        s.send_message(recipients)
        s.quit()


class Logger:
    def output(message):
        print(f"[Logger] {message}")


class LoggerAdapter:
    def __init__(self, what_it_have) -> None:
        self.what_i_have = what_it_have

    def send(self, sender, recipients, subject, message):
        log_message = f"From: {sender}\n To: {recipients}\nSubject: {subject}\nMessage: {message}"
        self.what_i_have.output(log_message)

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)


if __name__ == "__main__":
    user_fetcher = UserFetcher("users.csv")
    mailer = Mailer()
    mailer.send(
        "me@example.com",
        # esto falla ni lo voy a probar
        [x["email"] for x in user_fetcher.fetch_users()],
        "This is your message",
        "Have a good day"
    )
