import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "your api key"
NEWS_API_KEY = "your api key"


# Get yesterday's closing stock price.
stock_response = requests.get(STOCK_ENDPOINT, params={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
})
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

print(yesterday_closing_price)

# Get the day before yesterday's closing stock price.
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2 and percentage difference.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
difference_percentage = (difference / float(yesterday_closing_price)) * 100
print(f"{difference_percentage:.2f}%")

if difference_percentage > 5:
    news = requests.get(NEWS_ENDPOINT, params={
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    })
    articles = news.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {article['title']}\nDescription: {article['description']}" for article in
                      three_articles]
print(formatted_articles)


