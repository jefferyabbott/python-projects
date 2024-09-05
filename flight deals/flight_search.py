import requests
import os
from dotenv import load_dotenv
load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

class FlightSearch:
    def __init__(self):
        self.token = self._get_new_token()


    def _get_new_token(self):
        request_token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': os.getenv('AMADEUS_API_KEY'),
            'client_secret': os.getenv('AMADEUS_API_SECRET'),
        }
        response = requests.post(url=request_token_url, headers=header, data=body)
        response.raise_for_status()
        return response.json()['access_token']


    def lookup_iata_code(self, city):
        print(f"Getting IATA code for {city}")
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code

