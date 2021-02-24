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

grouped_df = df.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Value'],ascending=False).head(10)
print(grouped_df)
