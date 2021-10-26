import requests

# response=requests.get('https://www.cbr-xml-daily.ru/daily.xml')  
# print(response)
def exchange_rates(currency, format='full'):    
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'  
    response = requests.get(url).json()['Valute']    
    data = response[currency]     
    if format == 'full':    
        return data      
    elif format == 'value':    
        return data['Value']    

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')    
# print(response.text)  
currencies = response.json()
# print(currencies)
# print(currencies['Valute']['UAH'])
print(currencies['Valute']['CZK']['Name'])

# currency_name('R01700J')