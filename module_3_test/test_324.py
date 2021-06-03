import pandas as pd

# pd.set_option('display.max_columns', None) # вывод всех стобцов
data = pd.read_excel('./module_3_test/Fig3-1.xls', header=None,)  
print(data)
# data.info()
# with pd.ExcelFile('Fig3-1.xls') as xls:  
#     data['Sheet1'] = pd.read_excel(xls, 'Sheet1', na_values=['NA'])  
#     data['Sheet2'] = pd.read_excel(xls, 'Sheet2')  
# аналогично
# data = pd.read_excel('Fig3-1.xls', ['Sheet1', 'Sheet2'])  
# чтение по ссылке
data = pd.read_excel('http://www.econ.yale.edu/~shiller/data/Fig3-1.xls', header=None)  