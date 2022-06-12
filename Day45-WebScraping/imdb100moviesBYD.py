from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.imdb.com/list/ls020792672/")
imdb = response.text

IMDB = BeautifulSoup(imdb, "html.parser")
introduction = IMDB.title.string[0:-6]
print(introduction)
# imdb_all_movies = IMDB.select('div h3 a')
get_title = [score.getText() for score in IMDB.select('div h3 a')] #select (BS Documentation) - can be used to find tags beneath other tags

num = 0
with open('100Movies.txt', 'r+') as file:
    file.write(introduction)
    for item in get_title:
        num +=1
        file.write(f'\n{num}) {item}')