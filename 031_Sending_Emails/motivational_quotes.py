import smtplib
import datetime as dt
import random

SMTP_METHOD = "smtp.gmail.com"
MY_EMAIL = "example@email.com"
EMAIL_PASSWORD = "yourPassword22"

with open("quotes.txt") as file:
    quotes = file.readlines()

print(quotes)

def send_motivational_email():
    quote = random.choice(quotes)
    with smtplib.SMTP(SMTP_METHOD) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="salmansaeed1359@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )


weekday = dt.datetime.now().weekday()

if weekday == 0:  # Monday
    send_motivational_email()