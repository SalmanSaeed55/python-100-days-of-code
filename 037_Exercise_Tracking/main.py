import requests
import datetime

BASE_URL = "https://app.100daysofpython.dev"

API_KEY = "Your API Key"
APP_ID = "Your App ID"

REQUEST_URL_BASE = "https://api.sheety.co/df34641c094f25cab40ae2eae6817661/myWorkouts/workouts"

HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query = input("What exercise did you do today? ")

response_params = {
    "query": query,
    "gender": "Your Gender",
    "weight_kg": "Your Weight",
    "height_cm": "Your Height",
}

response = requests.post(url=f"{BASE_URL}/v1/nutrition/natural/exercise", headers=HEADER, json=response_params).json()

request_data = {
    "date": datetime.date.today().strftime("%Y/%m/%d"),
    "time": datetime.datetime.now().strftime("%H:%M:%S"),
    "exercise": response["exercises"][0]["name"].title(),
    "duration": response["exercises"][0]["duration_min"],
    "calories": response["exercises"][0]["nf_calories"],
}

add_row_request = requests.post(url=REQUEST_URL_BASE, json={"workout": request_data}, auth=("username", "password"))
print(add_row_request.text)
