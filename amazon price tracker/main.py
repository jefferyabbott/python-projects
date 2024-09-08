from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

TOTAL_CEREAL = "https://www.amazon.com/Total-Cereal-Whole-Grain-Box/dp/B000VDR3WO?pd_rd_w=jBCkZ&content-id=amzn1.sym.7e262374-44e5-4ab3-b618-0a09608861a6&pf_rd_p=7e262374-44e5-4ab3-b618-0a09608861a6&pf_rd_r=EDEFPE3PK3EC2VR9078R&pd_rd_wg=KOEj1&pd_rd_r=13389217-cd7e-4dbf-9792-f379ce6db2da&pd_rd_i=B000VDR3WO&psc=1&ref_=pd_bap_d_grid_rp_0_1_ec_cp_pd_hp_d_atf_rp_1_i"


def get_price():
    response = requests.get(TOTAL_CEREAL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML element that contains the price
    current_price = soup.find(class_="a-offscreen").get_text()
    price_without_currency = current_price.split("$")[1]
    return float(price_without_currency)


def send_email_alert(sale_price):
    my_email = os.getenv('MY_EMAIL')
    email_password = os.getenv('MY_EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    target_email = os.getenv('TARGET_EMAIL')

    with smtplib.SMTP(smtp_server, int(smtp_port)) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target_email,
            msg=f"Subject:Amazon Price Alert!\n\nThe pot is now ${sale_price}"
        )

price = get_price()
if price < 5:
    send_email_alert(price)
