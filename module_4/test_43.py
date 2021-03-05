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

# answers['10'] = '10. The Lone Ranger (tt1210819)'
# data_12_14 = data.query("release_year >= 2012 & release_year <= 2014")
# df = data_12_14.query("profit == {0}".format(data_12_14.profit.min()))[['imdb_id', 'original_title']]
# for index, row in df.iterrows():
#     print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))
# print(answers['10'])

# answers['11'] = '11. Drama'
# print('Action: {0}'.format(data[data.genres.str.contains('Action')].imdb_id.count()))
# print('Adventure: {0}'.format(data[data.genres.str.contains('Adventure')].imdb_id.count()))
# print('Drama: {0}'.format(data[data.genres.str.contains('Drama')].imdb_id.count()))
# print('Comedy: {0}'.format(data[data.genres.str.contains('Comedy')].imdb_id.count()))
# print('Thriller: {0}'.format(data[data.genres.str.contains('Thriller')].imdb_id.count()))
# print(answers['11'])

data['Action'] = data.genres.apply(lambda s:int('Action' in str(s))) 
data['Adventure'] = data.genres.apply(lambda s:int('Adventure' in str(s))) 
data['Drama'] = data.genres.apply(lambda s:int('Drama' in str(s))) 
data['Comedy'] = data.genres.apply(lambda s:int('Comedy' in str(s))) 
data['Thriller'] = data.genres.apply(lambda s:int('Thriller' in str(s))) 
# print(data[['Action', 'Adventure', 'Drama', 'Comedy', 'Thriller']].sum().sort_values(ascending=False))

# answers['12'] = '12. Drama'
# df = data.query("revenue > budget")
# print(df[['Action', 'Adventure', 'Drama', 'Comedy', 'Thriller']].sum().sort_values(ascending=False))
# print(answers['12'])

# answers['13'] = '13. Peter Jackson'
# print(data.groupby('director')['revenue'].sum().sort_values(ascending=False).head(1))
# print(answers['13'])

# answers['14'] = '14. '
# df = data.query("Action == 1")
# print(df.groupby('director')['imdb_id'].count().sort_values(ascending=False).head(2))
# print(answers['14'])
print('Nicolas Cage   : {0}'.format(data[data.cast.str.contains('Nicolas Cage')].revenue.sum()))

# df = data[data.genres.str.contains('Action')]
# print(df.groupby('director')['imdb_id'].count().sort_values(ascending=False).head(2))


# answers['15'] = '15. Chris Hemsworth'
# print('Nicolas Cage   : {0}'.format(data[data.cast.str.contains('Nicolas Cage')].revenue.sum()))
# print('Tom Hardy      : {0}'.format(data[data.cast.str.contains('Tom Hardy')].revenue.sum()))
# print('Chris Hemsworth: {0}'.format(data[data.cast.str.contains('Chris Hemsworth')].revenue.sum()))
# print('Jim Sturgess   : {0}'.format(data[data.cast.str.contains('Jim Sturgess')].revenue.sum()))
# print('Emma Stone     : {0}'.format(data[data.cast.str.contains('Emma Stone')].revenue.sum()))
# print(answers['15'])