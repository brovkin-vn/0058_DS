import pandas as pd
import numpy as np
import re
import datetime
import time
pd.set_option('display.max_columns', None) # вывод всех стобцов
df = pd.read_csv("./module_3/main_task_new.csv")
# df.info()
# print(df.isna().sum())
# print(df['Price Range'])
# print(df['Price Range'].unique())
# print(df['Price Range'].value_counts())
# print(len(list(df['City'].unique())))
# print(len(list(df['Cuisine Style'].unique())))
# print(df['Cuisine Style'].value_counts())pip

# cuisines = set()
# def qwe(row):
#     for v in row.to_list():
#         cuisines.add(v)

# df['Cuisine Style'].apply(qwe)
# print(len(cuisines))
# df['Cuisine Style'].fillna('[]')
# df['Cuisine Style'] = df['Cuisine Style'].str.split(',')
# print(df['Cuisine Style'])
# df = df.explode('Cuisine Style')
# df['Cuisine Style'] = df['Cuisine Style'].str.replace('[','')
# df['Cuisine Style'] = df['Cuisine Style'].str.replace(']','')
# df['Cuisine Style'] = df['Cuisine Style'].str.replace('\'','')
# df['Cuisine Style'] = df['Cuisine Style'].str.strip()
# print(df['Cuisine Style'].nunique())
# print(df['Cuisine Style'].value_counts())

# df['Cuisine Style'] = df['Cuisine Style'].str.replace('[','')
# df['Cuisine Style'] = df['Cuisine Style'].str.replace(']','')
# df['Cuisine Style'] = df['Cuisine Style'].str.split(',')
# df['Cuisine Style'] = df['Cuisine Style'].fillna('')
# df['cuisine_cnt'] = df['Cuisine Style'].apply(len)
# # df['cuisine_cnt'] = df['Cuisine Style'].apply(lambda x: if x == 0 return 1 else return x)
# print(df['cuisine_cnt'].mean())
# df.info()
# data = df
# def review_to_date(review):
#     pattern = re.compile('\'\d+\/\d+\/\d+\'?')
#     dat = pattern.findall(review)
#     if len(dat) >= 2:
#         datetime_list = []
#         for date in dat:
#             date = date[1:-1]
#             # dt = time.strptime(date, '%m/%d/%Y')
#             dt = date
#             datetime_list.append(dt)
#         return datetime_list
#     else:
#         return (dat)

# data['Reviews'] = data['Reviews'].astype(str)
# data['review_dates'] = data['Reviews'].apply(lambda x: review_to_date(x)) 
# # print(data['review_dates'])
# data = data.explode('review_dates')
# data['review_dates'] = pd.to_datetime(data['review_dates'])
# # print(data['review_dates'].max())
# dmax = data.groupby('Restaurant_id')['review_dates'].max()
# dmin = data.groupby('Restaurant_id')['review_dates'].min()
# dmm = pd.merge(dmax, dmin, on='Restaurant_id')  
# dmm['vv']= dmm.review_dates_x - dmm.review_dates_y
# print(dmm.groupby('Restaurant_id')['vv'].max())
# print(dmm['vv'].value_counts().max())


# df.info()
# print(df['City'].value_counts())
# print(df.groupby(['City'])['Number of Reviews'].mean().to_dict())
# df['Number of Reviews'].fillna(0, inplace=True)
# df['Number of Reviews'].fillna(round(df['Number of Reviews'].mean()), inplace=True)
# print(df['Cuisine Style'].isnan())
# print(df['Cuisine Style'].isnan())
# print(df['Price Range'].value_counts())
# df['Price Range'].fillna('$$ - $$$', inplace=True)
# df['Price Range'] = df['Price Range'].apply(lambda x: len(str(x)))
# df['Price_Range'] = df['Price Range']
# print(df['Price Range'].value_counts())
# df = pd.get_dummies(df, columns=[ 'Price Range'], dummy_na=False)

# df.info()

df['Cuisine Style'] = df['Cuisine Style'].str[2:-2].str.split(',')
df['Cuisine Style Num'] = df['Cuisine Style'].str.len()

print(df['Cuisine Style Num'])