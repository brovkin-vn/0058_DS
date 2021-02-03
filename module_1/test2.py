import pandas as pd
from IPython.display import display

# df = pd.DataFrame([[i,i+1.2,i+2, 'hi'] for i in range(10)],
#                   columns = ['foo', 'bar', 'baz', 'foobar'])
# display(df.foo)                  
# display(df.mean())

football = pd.read_csv('./data_sf.csv')
print(football.Age.mean())
print(football.Composure.describe())
# print(football.info())
print(round(football.ShortPassing.std(), 2))
print(football.Wage.sum())
print(football.Value.min())
print(football.Wage.avg())
