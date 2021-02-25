import pandas as pd
from IPython.display import display

df = pd.read_csv('../module_1/data_sf.csv')


grouped_df = df.groupby(['Club']).sum()
# display(grouped_df)

# print(grouped_df.loc['Ajax']['Wage'])

# grouped_df = df.groupby(['Club'])['Wage'].sum()
# display(grouped_df)

# grouped_df = df.groupby(['Club'])['Wage'].sum().sort_values(ascending=False)
# print(grouped_df.head(5))

# grouped_df = df.groupby(['Position'])['Wage'].sum().sort_values(ascending=False)
# print(grouped_df.loc[(grouped_df > 5000000)])

# grouped_df = df.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean()
# print(grouped_df)

# grouped_df = df.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean().sort_values(['Wage'],ascending=False).head(10)
# print(grouped_df)

# grouped_df = df.loc[df['Nationality'] == 'Dominican Republic'][['Name','Club','Wage','Age','ShotPower']]
# print(grouped_df)

# grouped_df = df.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Value'],ascending=False).head(10)
# print(grouped_df)

# print(df.groupby(['Nationality'])[['Club','Name']].nunique())

# print(df.groupby(['Club'])['Name'].count())
4
# print(df.groupby(['Club'])['Dribbling'].median())

# print(df.groupby(['Club'])['Strength'].max())

# print(df.groupby(['Club'])['Balance'].min())

# df1 = df.groupby(['Club'])['Wage'].agg(['mean','median'])
# # print(df1)

# df2 = df1.loc[(df1['mean'] == df1['median'])]
# print(df2)
# # print(df2.count())
# print( df2.sort_values(['median'],ascending=False) )

# df = df.loc[(df['Club'] == 'Chelsea')].groupby(['Club'])['Wage'].sum()
# print(df)
# df2 = df.loc[(df['Club'] == 'median')]
# print(df2)

# df = df.loc[(df['Nationality'] == 'Argentina') & (df['Age'] == 30)].sort_values(['Wage'],ascending=False)['Wage']
# print(df)

df = df.loc[(df['Nationality'] == 'Argentina') & (df['Club'] == 'FC Barcelona')][['Strength','Balance']]
print(df)

