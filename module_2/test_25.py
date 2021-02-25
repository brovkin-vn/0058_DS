import pandas as pd
from IPython.display import display

df = pd.read_csv('../module_1/data_sf.csv')

pivot = df.loc[df['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Wage'],
index=['Nationality'],
columns=['Club'],
aggfunc='sum')
display(pivot)