import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response.json()["iss_position"]["latitude"])

failed_response = requests.get(url="http://api.open-notify.org/iss-now.json")
failed_response.raise_for_status()

