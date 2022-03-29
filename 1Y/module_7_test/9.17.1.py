import requests  

token = '2bbc82c12bbc82c12bbc82c14e2bc687f122bbc2bbc82c14a3699ed37ba144c7f03d8a7'

def get_smm_index(group_name, token):
    url = 'https://api.vk.com/method/groups.getMembers'  
    params = {  
        'group_id': group_name,  
        'v': 5.95,  
        'access_token': token  
    }  
    response = requests.get(url, params = params)  
    data = response.json()  
    users  = data['response']['count']      

    url = 'https://api.vk.com/method/wall.get'  
    params = {  
        'domain': group_name,  
        'filter': 'owner',  
        'count': 10,  
        'offset': 0,  
        'access_token': token,  
        'v': 5.95  
    }  
    response = requests.get(url, params = params)  
    posts = response.json()['response']['items']
    sum = 0
    for post in posts:
        sum = sum + post['comments']['count'] + post['likes']['count'] + post['reposts']['count']
    
    

    return sum/users

print(get_smm_index('vk', token))