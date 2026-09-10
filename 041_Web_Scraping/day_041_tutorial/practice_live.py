from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.text, 'lxml')
news_titles = soup.find("span", class_="titleline").get_text()
print(news_titles)