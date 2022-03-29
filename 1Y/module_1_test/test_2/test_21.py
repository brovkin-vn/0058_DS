import pandas as pd
from IPython.display import display

df = pd.read_csv('../module_1/data_sf.csv')
small_df = df[df.columns[1:8]].head(25)

# s = df['Position'].value_counts(normalize=True)
# display(s)
# s = small_df['Age'].value_counts(bins=3)
# display(s)
# s = small_df['Wage'].value_counts(bins=4)
# display(s)

# display(small_df.loc[(small_df['Wage'] > s.index[3].left) & (small_df['Wage'] <= s.index[3].right)])

s = df['FKAccuracy'].value_counts(bins=5)
print(s)
