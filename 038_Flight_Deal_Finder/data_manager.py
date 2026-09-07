import requests

SHEETY_ENDPOINT = "https://api.sheety.co/df34641c094f25cab40ae2eae6817661/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._sheety_header = (
            "salman",
            "salman123"
        )
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self._sheety_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self._sheety_header
        )