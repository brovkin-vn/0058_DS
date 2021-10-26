import requests
from bs4 import BeautifulSoup    

# url = 'https://en.wikipedia.org/wiki/List_of_programming_languages'  
# response = requests.get(url)  
# page = BeautifulSoup(response.text, 'html.parser')  
# links = page.find_all('a')  
# l = [x.text for x in links]
# print(l[1:])

def get_actors(url):
    response = requests.get(url)  
    page = BeautifulSoup(response.text, 'html.parser')  
    links =  page.find_all('a', itemprop='actor')  
    return [x.text for x in links]


# url = 'https://www.kinopoisk.ru/film/435/'  
url = 'https://www.kinopoisk.ru/film/42326/'
print(get_actors(url))