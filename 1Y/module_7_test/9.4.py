# Импортируем наши библиотеки    
from bs4 import BeautifulSoup    
import requests    
    
# Получаем данные, как и ранее    
url = 'https://nplus1.ru/news/2019/06/04/slothbot'   
response = requests.get(url)    
    
# Теперь создадим объект BeautifulSoup, указывая html парсер    
page = BeautifulSoup(response.text, 'html.parser')    
    
# Всё готово, чтобы получать данные из страницы    
# Для начала получим title, отображающийся на закладках браузера    
print(page.title)  
# => <title>Робота-ленивца научили лазать по паутине из тросов</title>  
    
# Мы получили тэг. Чтобы достать из него текст, вызовем атрибут text    
page.title.text    
# => 'Робота-ленивца научили лазать по паутине из тросов'  
print(page.find('h1').text)   