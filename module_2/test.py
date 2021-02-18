import pandas as pd
from IPython.display import display

df = pd.read_csv('../module_1/data_sf.csv')

small_df = df[df.columns[1:8]].head(25)
# print(small_df)
# s = small_df['Nationality'].value_counts()
# display(s)
# print(len(s.index))
# print(s['Germany'])
# print(s.loc[s > 1])
# display(df)

s = df['Club'].value_counts()
display(s)
print(len(s.index))

