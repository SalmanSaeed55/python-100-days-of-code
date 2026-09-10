import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(response.text, 'lxml')

movie_titles = soup.find_all('h3', class_='title')
movie_list = [title.getText() for title in movie_titles]

movies_list = movie_list[::-1]  # Reverse the list to have the best movie at the top
print(movies_list)

with open('top_100_movies.txt', 'w', encoding='utf-8') as f:
    for movie in movies_list:
        f.write(f"{movie}\n")
