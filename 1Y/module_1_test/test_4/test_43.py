import pandas as pd
import itertools
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
# df = data.copy()
# df['genres'] = df['genres'].str.split('|')
# df = df.explode('genres')
# print(df.groupby('genres')['imdb_id'].count().sort_values(ascending=False))
# print(answers['11'])

# answers['12'] = '12. Drama'
# df = data.query("revenue > budget")
# df.genres = df.genres.str.split('|')
# df = df.explode('genres')
# print(df.groupby('genres')['imdb_id'].count().sort_values(ascending=False).head(1))
# print(answers['12'])

# answers['13'] = '13. Peter Jackson'
# df = data.copy()
# df.director = df.director.str.split('|')
# df = df.explode('director')
# print(data.groupby('director')['revenue'].sum().sort_values(ascending=False).head(1))
# print(answers['13'])

# answers['14'] = '14. Robert Rodriguez'
# df = data[data.genres.str.contains('Action')].copy()
# df.director = df.director.str.split('|')
# df = df.explode('director')
# print(df['director'].value_counts().head(1))
# print(answers['14'])



answers['15'] = '15. Chris Hemsworth'
df = data.query('release_year == 2012')
df.cast = df.cast.str.split('|')
df = df.explode('cast')
print(df.groupby('cast')['revenue'].sum().sort_values(ascending=False).head(1))
print(answers['15'])

# answers['16'] = '16. Matt Damon'
# df = data[(data.budget > data.budget.mean())]
# df.cast = df.cast.str.split('|')
# df = df.explode('cast')
# print(df['cast'].value_counts().head(1))
# print(answers['16'])

# answers['17'] = '17. Action'
# df = data[data.cast.str.contains('Nicolas Cage')].copy()
# df.genres = df.genres.str.split('|')
# df = df.explode('genres')
# print(df['genres'].value_counts().head(1))
# print(answers['17'])

# answers['18'] = '18. K-19: The Widowmaker (tt0267626)'
# df = data[data.production_companies.str.contains('Paramount Pictures')].copy()
# title = df[df.profit == df.profit.min()][['imdb_id', 'original_title']]
# for index, row in title.iterrows():
#     print("{0} ({1})".format(row['original_title'], row['imdb_id'], ))
# print(answers['18'])

# answers['19'] = '19. 2015'
# print(data.groupby('release_year')['revenue'].sum().sort_values(ascending=False).head(1))
# print(answers['19'])

# answers['20'] = '20. 2014'
# df = data[data.production_companies.str.contains('Warner Bros')].copy()
# print(df.groupby('release_year')['revenue'].sum().sort_values(ascending=False).head(1))
# print(answers['20'])

def return_month(release_date):
    m = int(str(pd.to_datetime(release_date)).split('-')[1])
    s = {
        1: "Январь",
        2: "Фервраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь"
    }
    s.setdefault(m, "Неверное значение")
    return s[m]
data['release_month'] = data.release_date.apply(return_month)

# answers['21'] = '21. 450'
# print(data.groupby('release_month')['imdb_id'].count().sort_values(ascending=False).head(1))
# print(answers['21'])

# answers['22'] = '22. 450'
# df = data.query('release_month == "Июнь" or release_month == "Июль" or release_month == "Август"')
# print(df.imdb_id.count())
# print(answers['22'])

# answers['23'] = '23. Peter Jackson'
# df = data.query('release_month == "Декабрь" or release_month == "Январь" or release_month == "Февраль"')
# df.director = df.director.str.split('|')
# df = df.explode('director')
# print(df['director'].value_counts().head(1))

# print(answers['23'])

# answers['24'] = '24. Four By Two Productions'
# df = data.copy()
# df['original_title_len'] = df.original_title.apply(lambda x:len(x))
# df['production_company'] = df.production_companies.str.split('|')
# df = df.explode('production_company')
# print(df.groupby('production_company')['original_title_len'].mean().sort_values(ascending=False).head(1))
# print(answers['24'])

# answers['25'] = '25. Midnight Picture Show'
# df = data.copy()
# df['overview_len'] = df.overview.apply(lambda x:len(str(x).split()))
# df['production_company'] = df.production_companies.str.split('|')
# df = df.explode('production_company')
# print(df.groupby('production_company')['overview_len'].mean().sort_values(ascending=False).head(1))
# print(answers['25'])

# answers['26'] = '26. Inside Out, The Dark Knight, 12 Years a Slave'
# df = data.copy()
# print(df.groupby('original_title')['vote_average'].mean().sort_values(ascending=False).head(19))
# print(answers['26'])


# answers['27'] = '26. Daniel Radcliffe & Emma Watson'
# df = data.copy()
# df.cast = df.cast.str.split('|').apply(lambda x:list(itertools.combinations(x, 2)))
# df = df.explode('cast')
# print(df.cast.value_counts().head(1))
# print(answers['27'])
