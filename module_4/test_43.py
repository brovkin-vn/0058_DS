import pandas as pd
from IPython.display import display

data = pd.read_csv('module_4/movie_bd_v5.csv')
data['profit'] = data['revenue'] - data['budget']
answers = {}

# print(data.runtime.max())
print(data.columns)
# print(data.budget)
# pd.set_option('display.max_columns', None) 
# print(data.loc[(data['budget'] == data.budget.max())][['imdb_id', 'original_title']])

# title = data[data.budget == data.budget.max()][['imdb_id', 'original_title']]
# for index, row in title.iterrows():
#     print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))

# print(data.loc[(data['runtime'] == data.runtime.max())][['imdb_id', 'original_title']])

# title = data[data.runtime == data.runtime.max()][['imdb_id', 'original_title']]
# for index, row in title.iterrows():
#     print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))

# df = data.query("runtime == {0}".format(data.runtime.max()))[['imdb_id', 'original_title']]
# print(df)

# df = data.query("runtime == {0}".format(data.runtime.min()))[['imdb_id', 'original_title']]
# for index, row in df.iterrows():
#     print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))

# print(round(data.runtime.mean()))
# print(round(data.runtime.median()))


# answers['6'] = '6. Avatar (tt0499549)'
# df = data.query("profit == {0}".format(data.profit.max()))[['imdb_id', 'original_title']]
# for index, row in df.iterrows():
#     print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))
# print(answers['6'])

# answers['7'] = '7. The Lone Ranger (tt1210819)'
# df = data.query("profit == {0}".format(data.profit.min()))[['imdb_id', 'original_title']]
# for index, row in df.iterrows():
#     print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))
# print(answers['7'])

# answers['8'] = '8. 1478'
# data['profit'] = data['revenue'] - data['budget']
# df = data.query("revenue > budget")['imdb_id']
# print(df.count())
# print(answers['8'])


# answers['9'] = '9. The Dark Knight (tt0468569)'
# data_2008 = data.query("release_year == 2008")
# df = data_2008.query("profit == {0}".format(data_2008.profit.max()))[['imdb_id', 'original_title']]
# for index, row in df.iterrows():
#     print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))
# print(answers['9'])

answers['10'] = '10. The Lone Ranger (tt1210819)'
data_12_14 = data.query("release_year >= 2012 & release_year <= 2014")
df = data_12_14.query("profit == {0}".format(data_12_14.profit.min()))[['imdb_id', 'original_title']]
for index, row in df.iterrows():
    print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))
print(answers['10'])


