import requests
import twilio.rest


account_id = "your account code"
authentication_token = "your authentication token"

api_key = "your api key"
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
