# import pandas as pd

# url = 'https://www.banki.ru/banks/ratings/'  
# df = pd.read_html(url)[0]
# print(df)

from bs4 import BeautifulSoup  
import pandas as pd  
import requests  
  
url = 'https://www.cbr.ru/key-indicators/'
soup = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text, 'html.parser')  


all_blocks = soup.find_all('div', class_='key-indicator_content offset-md-2')
# Данные таблицы с драгметаллами находятся во втором блоке
data = all_blocks[1].find('table') 

df = pd.read_html(str(data))[0]  
print(df)