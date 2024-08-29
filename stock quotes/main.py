import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

def get_news(company):
    news_api_params = {
        "q": company,
        "pageSize": 3,
        "apiKey": os.getenv('NEWS_API_KEY'),
    }

    news_api_url = "https://newsapi.org/v2/everything"

    news_resp = requests.get(url=news_api_url, params=news_api_params)
    news_resp.raise_for_status()
    news_data = news_resp.json()['articles']
    news_items = []
    for item in news_data:
        news_items.append(item['description'])
    return news_items


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then get news.
alpha_vantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": os.getenv('ALPHA_VANTAGE_API_KEY'),
    "limit": 2,
}

alpha_vantage_url = 'https://www.alphavantage.co/query'

stock_resp = requests.get(url=alpha_vantage_url, params=alpha_vantage_params)
stock_resp.raise_for_status()
stock_data = stock_resp.json()

closing_date = list(stock_data['Time Series (Daily)'].keys())[0]
previous_closing_date = list(stock_data['Time Series (Daily)'].keys())[1]
closing_price = stock_data['Time Series (Daily)'][closing_date]['4. close']
previous_closing_price = stock_data['Time Series (Daily)'][previous_closing_date]['4. close']
percent_change = ((closing_price - previous_closing_price) / closing_price) * 100

if percent_change >= 5 or percent_change <= -5:
    stock_news = get_news(COMPANY_NAME)
    client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    for article in stock_news:
        arrow = ""
        if percent_change > 0:
            arrow = "🔺"
        if percent_change < 0:
            arrow = "🔻"
        message_text = f"{COMPANY_NAME}: {arrow} {int(percent_change)}%\n{article}"
        message = client.messages.create(
            body=message_text,
            from_=os.getenv('TWILIO_NUMBER'),
            to=os.getenv('TWILIO_RECIPIENT'),
        )
        print(message.status)

