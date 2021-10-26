import requests  
  
url = 'https://nplus1.ru/news/2019/06/04/slothbot'   
  
response = requests.get(url)  
  
# Убедимся, что мы успешно получили ответ     
print(response.status_code)    
# => 200   
  
# Выведем полученные данные    
print(response.text)   
  