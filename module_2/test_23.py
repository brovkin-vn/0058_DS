import pandas as pd
from IPython.display import display

df = pd.read_csv('../module_1/data_sf.csv')

# s = df['Nationality'].value_counts()
# df_spain = df.loc[(df['Nationality'] == 'Spain')]
# s = df_spain['Wage'].value_counts(bins=4, normalize=True)
# print(s)

# df_club = df.loc[(df['Club'] == 'Manchester United')]
# s = df_club['Nationality'].nunique()
# print(s)

# s = df['Nationality'].value_counts()
# df_brazil = df.loc[(df['Nationality'] == 'Brazil') & (df['Club'] == 'Juventus')]
# s = df_brazil['Name'].unique()
# print(s)

# df_age = df.loc[(df['Age'] > 35)]
# s = df_age['Club'].value_counts()
# print(s)

# df_arg = df.loc[(df['Nationality'] == 'Argentina')]
# s = df_arg['Age'].value_counts(bins=4)
# print(s)

df_spain = df.loc[(df['Nationality'] == 'Spain')]
s = df_spain['Age'].value_counts(normalize=True)
print(s)


