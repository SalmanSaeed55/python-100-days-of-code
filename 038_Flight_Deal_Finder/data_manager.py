import requests
import requests_cache

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = "salman"
        self.password = "salman123"
        self.SHEETY_URL_GET = "https://api.sheety.co/df34641c094f25cab40ae2eae6817661/flightDeals/prices"

    def get_destination_data(self):
        response = requests.get(self.SHEETY_URL_GET, auth=(self.username, self.password))
        return response.json()
