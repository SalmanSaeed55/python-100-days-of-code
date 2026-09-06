# Module Imports
import requests_cache
from pprint import pprint
from datetime import datetime, timedelta

# Class Imports
from data_manager import DataManager
from flight_search import FlightSearch

# Set up caching to save API limits
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

# Set up today's date and date for 6 months later
today = datetime.now()
six_months_later = today + timedelta(days=(6 * 30))

# Initialize DataManager and get destination data
sheet_data = DataManager()
pprint(sheet_data.get_destination_data())

# Initialize FlightData and check flight deals for each destination
flight_data = FlightSearch()
print(flight_data.check_flight("MAN", "JED", today.strftime("%Y-%m-%d"), six_months_later.strftime("%Y-%m-%d")))