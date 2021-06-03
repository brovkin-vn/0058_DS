import pandas as pd

pd.set_option('display.max_columns', None) # вывод всех стобцов
data = pd.read_excel("./module_3_test/nakladnaya.xls", header=None, skiprows=2, na_values=['NA'])
# Чтобы убирать только те строки, в которых все значения являются пропусками, нужно использовать параметр how и передавать в него значение all.
data = data.dropna(axis=0, how='all')
# data = data.dropna(axis=1, how='all')
print(data)
print(data.iloc[0, 4][2:9])
print(len(list(data.iloc[7].dropna())))
print(data.iloc[7])
print(1,data.iloc[6:8, [1, 2, 6, 9, 11, 12]])
print(2,data.iloc[6:8, [0, 2, 6, 9, 11, 12]])
print(3,data.iloc[7:8, :].dropna(axis=1, how='all'))
print(4,data.iloc[6:8, :].dropna(axis=1, how='any'))
print(5,data.iloc[6:8, :].dropna(axis=1, how='all'))
table = data.iloc[6:8, :].dropna(axis=1, how='all')
print('table\n', table)
table.to_excel("./module_3_test/table.xls", index=False)  
# writer = pd.ExcelWriter('/module_3_test/test.xlsx')  
# workbook = writer.book  
# worksheet = writer.sheets['Таблица'] 
# money_fmt = workbook.add_format({'bold': True})  
# name_fmt = workbook.add_format({'color': 'red'})  
  
# worksheet.set_column('E:F', 20, money_fmt)  
# worksheet.set_column(1, 1, 20, name_fmt) 
# table.to_excel(writer, index=False, sheet_name='Таблица')  
# writer.save()  
