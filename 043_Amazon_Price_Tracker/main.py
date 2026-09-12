from bs4 import BeautifulSoup
import requests
from pprint import pprint
import lxml
import smtplib

email = "your_email@gmail.com"
password = "your_password"

# 1. Get the HTML content of the webpage
response = requests.get("https://appbrewery.github.io/instant_pot/")
soup = BeautifulSoup(response.content, "lxml")

# 2. Find the price element in the HTML
price = soup.find(name="span", class_="aok-offscreen").getText().split("$")[1]
float_price = float(price)

print(float_price)

# 3. Find the title of the product
title = soup.find(id="productTitle").get_text().strip()
pprint(title)

BUY_PRICE = 100

if float_price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    url = "https://appbrewery.github.io/instant_pot/"

    # 4. Send an email notification
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

