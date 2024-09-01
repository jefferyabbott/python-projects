import requests
import os
from dotenv import load_dotenv
load_dotenv()
from pprint import pprint

# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
        }
        self.url = f"https://api.sheety.co/{os.getenv('SPREADSHEET')}/flightDeals/prices"

    def get_sheet(self):
        try:
            response = requests.get(url=self.url, headers=self.headers)
            # pprint(response.json())
            return response.json()['prices']
        except:
            return "Google sheet not available."

    def update_iata_code(self, id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code,
            }
        }
        try:
            response = requests.put(url=f"{self.url}/{id}", headers=self.headers, json=body)
            print(response.json())
        except:
            print("Google sheet not available")


