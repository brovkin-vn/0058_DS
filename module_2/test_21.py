import pandas as pd
from IPython.display import display

df = pd.read_csv('../module_1/data_sf.csv')

small_df = df[df.columns[1:8]].head(25)
s = small_df['Nationality'].value_counts(normalize=True)
display(s)
