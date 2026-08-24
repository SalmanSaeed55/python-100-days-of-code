import requests

api_key = "5afecd78fa382140cdde8c9da6c70ea7"
api_url = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": 51.5074,
    "lon": 0.1278,
    "appid": api_key,
    "units": "metric",
    "lang": "en",
    "cnt": 4,
}

weather_response = requests.get(api_url, params=weather_params)
weather_response.raise_for_status()
weather_data = weather_response.json()
print(weather_data)
