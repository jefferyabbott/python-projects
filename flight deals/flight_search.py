import requests
import os
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer ${os.getenv('AMADEUS_API_KEY')}"
        }
        self.base_url = "https://test.api.amadeus.com/v1/reference-data/locations"


    def lookup_iata_code(self, city):
        print("lookup ", city)
        return "TESTING"

