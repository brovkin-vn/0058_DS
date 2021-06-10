import pandas as pd
import numpy as np
import re
import datetime
import time
pd.set_option('display.max_columns', None) # вывод всех стобцов
df = pd.read_csv("./module_3/main_task_new.csv")

df.rename(
    columns={'Cuisine Style': 'Cuisine_Style', 'Price Range': 'Price_Range', 'Number of Reviews': 'Number_of_Reviews'}, inplace=True)
# df.info()

# print(df.Restaurant_id.value_counts())
# df.Number_of_Reviews.fillna(round(df.groupby(['City'])['Number_of_Reviews'].transform('mean')), inplace=True)

# df.Cuisine_Style = df.Cuisine_Style.str[2:-2].str.split(',')

# df.Reviews = df.Reviews.str[2:-2].str.replace('], ',']').str.replace('][','|')
# print(df.Reviews.head(2))
# s = "[['aaaa', 'bbbb'], ['1111', '2222']]"
# print(s)
# print(s[2:-2])
# print(s[2:-2].replace('], [','|'))
# print(s[2:-2].replace('], [','|').split('|'))
# print(s[2:-2].replace('], [','|').split('|')[0].split(','))
# print(s[2:-2].replace('], [','|').split('|')[1].split(','))

def prepare_reviews(s):
    l = s[2:-2].replace('], [','|').split('|')
    v0 = l[0].split(',')
    v1 = l[1].split(',')
    return [v0, v1] 

# print(prepare_reviews(str(s)))
# print(df.Reviews[0])
df.Reviews = df.Reviews.map(lambda x: prepare_reviews(str(x)))
# print(df.Reviews)

# print(df.Restaurant_id.value_counts())

df.Cuisine_Style.fillna('other', inplace=True)
df.Cuisine_Style = df.Cuisine_Style.str[2:-2].str.split(',')
# print(df['Cuisine_Style'].head(2))
df['Cuisine_Style_Num'] = df.Cuisine_Style.str.len()
# print(df['Cuisine_Style_Num'].head(2))

rr = df.City.value_counts().to_dict()
# print(rr)
tmp_dict = df.City.value_counts().to_dict()
df['Restaurant_num'] = df['City'].map(tmp_dict)
# print(df.Restaurant_num.head(5))
tmp_dict = df.Restaurant_id.value_counts().to_dict()
df['Network_size'] = df['Restaurant_id'].map(tmp_dict)
df['Network'] = df['Network_size'].apply(lambda x: 0 if (x == 1) else 1)
# print(df.Network.head(50))
# df['Network'] = df.Restaurant_id.map(lambda x: )
print(df.Reviews.head(1))
df['Reviews_Dates'] = df.Reviews.apply(lambda x: x[1])
df['Reviews_Date1'] = df.Reviews_Dates.apply(lambda x: x[0])
df['Reviews_Date2'] = df.Reviews_Dates.apply(lambda x: x[-1])
df['Reviews_Date1'] = pd.to_datetime(df['Reviews_Date1'], errors='coerce')
df['Reviews_Date2'] = pd.to_datetime(df['Reviews_Date2'], errors='coerce')
dmax = df.Reviews_Date2.max()
dmin = df.Reviews_Date1.min()
df['Reviews_Days_Delta_Min'] = (dmax - df.Reviews_Date2).dt.days
df['Reviews_Days_Delta_Max'] = (dmax - df.Reviews_Date1).dt.days
df.Reviews_Days_Delta_Max.fillna(df.Reviews_Days_Delta_Max.mean(), inplace=True)
df.Reviews_Days_Delta_Min.fillna(df.Reviews_Days_Delta_Min.mean(), inplace=True)
# df['Reviews_Days_Delta_Max'] = (df.Reviews_Date_Max - df.Reviews_Date1).dt.days
# print(dmin, dmax)


# print(df.Reviews_Dates.head(2))
# print(df.Reviews_Days_Delta_Max.head(2))
# print(df.Reviews_Days_Delta_Min.head(2))
# print(df.Reviews_Days_Delta_Min.value_counts())

df['Reviews_Words'] = df.Reviews.apply(lambda x: x[0])
df['Reviews_Words'] = df.Reviews.apply(lambda x: x[0])
print(df.Reviews_Words.head(2))


df.info()