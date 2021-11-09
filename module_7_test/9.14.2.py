import requests  
  
url = 'https://api.vk.com/method/users.get'   
token = '2bbc82c12bbc82c12bbc82c14e2bc687f122bbc2bbc82c14a3699ed37ba144c7f03d8a7'
ids = ",".join(map(str, range(1, 501)))  
params = {'user_ids': ids, 'v': 5.95, 'fields': 'sex', 'access_token': token, 'lang': 'ru'}  




response = requests.get(url, params=params)  

users = response.json()['response']

w = 0
cnt = 500
for user in users:
    if user['sex'] == 1:
        w = w + 1
    if user['sex'] == 0:
        cnt = cnt - 1
    # print(user['sex'])

print(users[0]['sex'])  
print(round(w/cnt, 2))



