import requests
import twilio.rest


account_id = "ACb1ef4499aa267fc9a54e89fe902f3f79"
authentication_token = "f55dc232c1bbbde73211d258661464a0"

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

will_rain = False
for weather in weather_data["weather"]:
    if "rain" in weather["main"].lower():
        will_rain = True

if will_rain:
    print("It's going to rain today. Remember to bring an umbrella ☔")
    client = twilio.rest.Client(account_id, authentication_token)
    message = client.messages.create(
        to="whatsapp:+447823712753",
        from_="whatsapp:+447723317807",
        body="It's going to rain today. Remember to bring an umbrella ☔"
    )
    print(message.status)
