import pandas as pd
from IPython.display import display

data = pd.Series(list(range(10, 1001)))
 
print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

display(df)


football = pd.read_csv('./data_sf.csv')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(football.describe())


display(football.describe(include = ['object']))