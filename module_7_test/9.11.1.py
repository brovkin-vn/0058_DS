# import requests
# from bs4 import BeautifulSoup    
import pandas as pd

url = 'https://www.cbr.ru/key-indicators/'  
# Таблица с драгметаллами оказалась второй по счёту  
tables = pd.read_html(url)
print(tables[0])