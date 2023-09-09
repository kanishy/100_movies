from bs4 import BeautifulSoup
import requests


website = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
responce = requests.get(website)
content = responce.text

soup = BeautifulSoup(content, "html.parser")
names = soup.find_all(name="h3", class_="title")

movies = []
for name in names:
    try:
        movies.append(name.get_text().split(")")[1])
    except:
        movies.append(name.get_text().split(":")[1])
file = open("movies.txt", "w", encoding="utf=8")
for i in range(99, -1, -1):
    index = 100 - i
    text = f"{index})"+movies[i]+"\n"
    file.write(text)
file.close()