import datetime as dt
import smtplib
from contextlib import nullcontext
from random import choice
import os
from dotenv import load_dotenv

load_dotenv()


def pick_a_quote():
    try:
        with open('quotes.txt') as quote_file:
            quote_data = quote_file.readlines()
    except FileNotFoundError:
        return ""
    return choice(quote_data)


def email_quote(quote):
    my_email = os.getenv('MY_EMAIL')
    email_password = os.getenv('MY_EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')

    with smtplib.SMTP(smtp_server, int(smtp_port)) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jeff@jefferyabbott.com",
            msg=f"Subject:Your quote for today\n\n{quote}"
        )


now = dt.datetime.now()
if now.weekday() == 6:
    quote_of_the_day = pick_a_quote()
    if quote_of_the_day != "":
        email_quote(quote_of_the_day)
