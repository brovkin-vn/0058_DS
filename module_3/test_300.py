import pandas as pd
pd.set_option('display.max_columns', None) # вывод всех стобцов
df = pd.read_csv("./module_3/main_task_new.csv")
# df.info()
# print(df.isna().sum())
# print(df['Price Range'])
# print(df['Price Range'].unique())
# print(df['Price Range'].value_counts())
# print(len(list(df['City'].unique())))
print(len(list(df['Cuisine Style'].unique())))
print(df['Cuisine Style'].value_counts())
