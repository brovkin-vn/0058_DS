from bs4 import BeautifulSoup    
import requests    
    
url = 'https://en.wikipedia.org/wiki/Operating_system'   
response = requests.get(url)    
    
page = BeautifulSoup(response.text, 'html.parser')    
    
print(page.find('h1').text)   

def wiki_header(url):
    response = requests.get(url)    
    page = BeautifulSoup(response.text, 'html.parser')    
    return page.find('h1').text   

print(wiki_header('https://en.wikipedia.org/wiki/Operating_system'))


value=page.find('span',id_='target').text  
value=page.find('class', class_
print(value)