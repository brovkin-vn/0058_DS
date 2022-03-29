import pandas as pd
from IPython.display import display

df = pd.read_csv('../module_1/data_sf.csv')

# pivot = df.loc[df['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Wage'],
# index=['Nationality'],
# columns=['Club'],
# aggfunc='sum',
# margins=True)
# display(pivot)

# df2 = df.pivot_table(columns = 'Position', index = 'Club', values = 'Wage', aggfunc = 'max')
# print(df2.loc['Manchester City']['GK'])

# Заполнение пустых значений
# pivot = df.loc[df['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Wage'],
# index=['Nationality'],
# columns=['Club'],
# aggfunc='sum',
# margins=True,
# fill_value=0)
# display(pivot)

# # Подсчет количества футболистов по клубам и национальностям
# pivot = df.loc[df['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Name'],
# index=['Nationality'],
# columns=['Club'],
# aggfunc='count',
# fill_value=0)
# display(pivot)

# # Обращение к элементу сводной таблицы
# print(pivot.loc['Argentina']['Name']['Manchester United'])

# Количество игроков занимающих разные позииции в каждом клубе
# df2 = df.pivot_table(columns = 'Position', index = 'Club', values = 'Wage', aggfunc = 'count', fill_value=0)
# # print(df.groupby(['Club'])['Balance'].min())
# print(df2['GK'].mean())
# df2 = df2.loc[(df2['CM'] == 0)]['CM']
# print(df2.value_counts())

# Создайте сводную таблицу, содержащую сведения о средней скорости футболистов (SprintSpeed)
# , занимающих разные позиции (Position) в разных футбольных клубах (Club).

df = df.pivot_table(columns = 'Position', index = 'Club', values = 'SprintSpeed', aggfunc = 'mean', fill_value=0)
# print(df.max().sort_values(ascending=False))

# Используя таблицу, созданную на предыдущем шаге, 
# отметьте названия трёх клубов, в которых центральные форварды (ST) 
# обладают наибольшей средней скоростью.
print(df['ST'].sort_values(ascending=False).head(3))


