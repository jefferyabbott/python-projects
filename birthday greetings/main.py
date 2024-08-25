import pandas
import datetime as dt
from random import randint
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


# Check if today matches a birthday in the birthdays.csv
# return a list of all of today's birthdays
def search_for_birthdays_today():
    todays_birthdays = []
    try:
        data = pandas.read_csv('birthdays.csv')
    except FileNotFoundError:
        return todays_birthdays
    birthday_data = data.to_dict(orient="records")
    now = dt.datetime.now()
    day = now.day
    month = now.month
    for birthday in birthday_data:
        if birthday['month'] == month and birthday['day'] == day:
            todays_birthdays.append(birthday)
    return todays_birthdays


# generate random birthday letter
def generate_random_birthday_letter(b_name):
    random_number = randint(1, 3)
    template_file = f"letter_templates/letter_{random_number}.txt"
    try:
        with open(template_file) as file:
            template = file.read()
    except FileNotFoundError:
        return ''
    return template.replace('[NAME]', b_name)


# Send the letter
def email_birthday_greeeting(name, email, msg):
    my_email = os.getenv('MY_EMAIL')
    email_password = os.getenv('MY_EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')

    with smtplib.SMTP(smtp_server, int(smtp_port)) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy birthday {name}!\n\n{msg}"
        )


birthdays = search_for_birthdays_today()

for birthday in birthdays:
    letter = generate_random_birthday_letter(birthday['name'])
    if letter != '':
        email_birthday_greeeting(birthday['name'], birthday['email'], letter)
