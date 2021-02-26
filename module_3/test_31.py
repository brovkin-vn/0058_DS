import pandas as pd
from IPython.display import display

ratings = pd.read_csv('module_3/ratings.csv')
movies = pd.read_csv('module_3/movies.csv')
# print(ratings.head())
# print(movies.head())

# print(ratings.count())
# print(ratings['rating'].max())
# print(movies['title'].count())

# joined = ratings.merge(movies, on='movieId', how='outer')
# print(joined.head())
# print(joined.head())
# print(len(ratings) == len(joined))

# Сколько раз была выставлена низшая оценка 0.5 в наших рейтингах? Используйте файл ratings.csv.
# print(ratings.loc[(ratings['rating'] == 0.5)].count())

# Объедините датафреймы ratings и movies, используя параметр how='outer'.
joined = ratings.merge(movies, on='movieId', how='outer')
# print(joined.count())

# Найдите в датафрейме movies фильм с movieId=3456.
print(joined.loc[(joined['movieId']==3456)])



