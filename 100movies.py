from bs4 import BeautifulSoup

import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_list = response.text
soup = BeautifulSoup(movies_list, "html.parser")

movie_names = [name.getText() for name in soup.find_all(name="h3", class_="title")]
movies = (movie_names[::-1])
# print(movies)
with open("movies_list.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}s\n")
