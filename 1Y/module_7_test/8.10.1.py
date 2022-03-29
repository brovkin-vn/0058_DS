import pandas as pd

df = pd.read_csv('module_7_test/imdb.csv')
df.info()
df2 = df[(df.Title == 'Suicide Squad')]
print(df2.Year)

print(repr('12.48'))

