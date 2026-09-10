from bs4 import BeautifulSoup
import lxml

with open("website.html", "r") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")
print(soup.title)

all_anchors = soup.find_all('a')
print(all_anchors)

for anchor in all_anchors:
    print(anchor.getText())

heading = soup.find(name="h1", id="name")
print(heading)