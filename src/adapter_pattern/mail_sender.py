import csv
import smtplib

from email.mime.text import MIMEText

from adapter_pattern.user_fetcher import UserFetcher


class Mailer:

    def send(sender, recipients, subject, message):

        msg = MIMEText(message)

        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = [recipients]

        s = smtplib.SMTP('localhost')
        s.send_message(recipients)
        s.quit


if __name__ == "__main__":
    with open('user.csv', 'r') as csv_file:
        user_fetcher = UserFetcher('users.csv')
        mailes = Mailer()

        mailer.send(
            'me@example.com',
            [x['email'] for x in user_fetcher.fetch_users()],
            "This is your message",
            "Have a good day",
        )
