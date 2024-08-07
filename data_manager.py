import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/b237e38ca30d773f18ac9108cc89a109/flightDeals/prices"
PUT_SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/b237e38ca30d773f18ac9108cc89a109/flightDeals/prices/IATA Code"
class DataManager:

    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self.authorization)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city["id"]}",
                auth=self.authorization,
                json=new_data
            )