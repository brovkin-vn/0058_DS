import pandas as pd
from IPython.display import display

ratings = pd.read_csv('module_3/ratings.csv')
movies = pd.read_csv('module_3/movies.csv')
# print(ratings.head())

# print(movies.head())
# print(ratings.count())
print(ratings['rating'].max())

