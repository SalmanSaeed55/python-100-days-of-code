# import smtplib
#
# SMTP_METHOD = "smtp.gmail.com"
# MY_EMAIL = "salmansaeed@gmail.com"
# EMAIL_PASSWORD = "gathorne2021"
#
# with smtplib.SMTP(SMTP_METHOD) as connection:
#     connection.starttls()
#     connection.login(MY_EMAIL, EMAIL_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="salmansaeed1359@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
day = now.day
hour = now.hour
