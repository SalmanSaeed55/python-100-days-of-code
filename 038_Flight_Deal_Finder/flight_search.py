import requests

SERP_API_KEY = "beebb23e436267dad1354047c6cfa4c0105184305947e1aa65416b7148a220e6"


class FlightSearch:

    def __init__(self):
        self._serp_api_key = SERP_API_KEY
        self._serp_api_endpoint = "https://serpapi.com/search?engine=google_flights"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._serp_api_key,
        }

        response = requests.get(url=self._serp_api_endpoint, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data
