import pandas as pd
from IPython.display import display

df = pd.read_csv('../module_1/data_sf.csv')
small_df = df[df.columns[1:8]].head(25)

# s = small_df['Nationality'].value_counts()
# print(s.index)
# print(len(s.index))

# print(small_df['Nationality'].unique())
# print(len(small_df['Nationality'].unique()))

# result = len(df['Position'].unique)
# result = df['Position'].nunique()
# print(1, result)
# result = len(df['Position'].unique())
# print(2, result)
# result = df['Position'].unique()
# print(3, result)
# result = df['Position'].count()
# print(4, result)
# result = len(df['Position'].value_counts())
# print(5, result)

# s = small_df['Nationality'].value_counts()
# s_df = s.reset_index()
# s_df.columns = ['Nationality','Players Count']
# display(s_df)

