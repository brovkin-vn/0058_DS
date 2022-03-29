import requests  
  
url = 'https://api.vk.com/method/users.get'   
token = '2bbc82c12bbc82c12bbc82c14e2bc687f122bbc2bbc82c14a3699ed37ba144c7f03d8a7'
params = {'user_id': 1, 'v': 5.95, 'fields': 'sex,bdate', 'access_token': token, 'lang': 'ru'}  
  
# Мы можем выставить параметры запроса через аргумент params  
response = requests.get(url, params=params)  
print(response.json())
user = response.json()['response'][0]  
  
# Выведем дату рождения  
print(user['bdate'])  
# => 10.10.1984  
  
# Выведем имя  
print(user['first_name'])  
# => Павел  

ids = ",".join(map(str, range(1, 4)))  
print(ids)  
# => 1,2,3  
  
params = {'user_ids': ids, 'v': 5.95, 'fields': 'bday', 'access_token': token, 'lang': 'ru'}  
  
print(requests.get(url, params=params).json()) 