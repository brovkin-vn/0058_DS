import requests

def currency_name(ID):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')    
    currencies = response.json()
    result = ''
    for key in currencies['Valute']:
        if currencies['Valute'][key]['ID'] == ID:
            result = currencies['Valute'][key]['Name']
            break
    
    return result


print(currency_name('R01700J'))