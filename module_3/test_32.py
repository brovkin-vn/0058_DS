import pandas as pd
from IPython.display import display

ratings = pd.read_csv('module_3/ratings_example.txt', sep = '\t')
movies = pd.read_csv('module_3/movies_example.txt', sep='\t')
# print(ratings.head())
# print(movies.head())

# joined = ratings.merge(movies, on='movieId', how='left')
print('left')
print(ratings.merge(movies, on='movieId', how='left'))
print('right')
print(ratings.merge(movies, on='movieId', how='right'))
print('inner')
print(ratings.merge(movies, on='movieId', how='inner'))
print('outer')
print(ratings.merge(movies, on='movieId', how='outer'))

# movies.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)
# print(ratings.merge(movies, how = 'left', on = 'movieId'))