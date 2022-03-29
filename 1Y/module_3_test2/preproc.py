import pandas as pd
import numpy as np
import re
import datetime
import time

class Preproc():

    def __init__(self, df):
        # df = df.copy(df)
        df = self.prepare(df)
        df = self.fill_nan(df)
        df = self.encoding(df)
        df = self.make_feuture(df)
        df = self.make_dammies(df)
        df = self.clean(df)
        self.df = df

    def prepare(self, df):
        # ################### 1. Предобработка ############################################################## 
        # переименование колонок для удобства
        df.rename(
            columns={'Cuisine Style': 'Cuisine_Style', 'Price Range': 'Price_Range', 'Number of Reviews': 'Number_of_Reviews'}, inplace=True)

        return df
    
    
    def fill_nan(self, df):
        # ################### 2. NAN ############################################################## 
        # Далее заполняем пропуски, вы можете попробовать заполнением средним или средним по городу и тд...
        df.Number_of_Reviews.fillna(round(df.Number_of_Reviews.mean()), inplace=True)
        # df.Number_of_Reviews.fillna(round(df.groupby(['City'])['Number_of_Reviews'].transform('mean')), inplace=True)
        df['Number_of_Reviews_isNAN'] = pd.isna(df.Number_of_Reviews).astype('uint8')
        
        # Cuisine Style
        df['Cuisine_Style_isNAN'] = pd.isna(df.Cuisine_Style).astype('uint8')
        df.Cuisine_Style.fillna('other', inplace=True)

        df['Price_Range_isNAN'] = pd.isna(df.Price_Range).astype('uint8')
        df.Price_Range.fillna('$$ - $$$', inplace=True)
    
        df['Reviewse_isNAN'] = pd.isna(df.Reviews).astype('uint8')
        df.Reviews.fillna('[[], []]', inplace=True)
    
        return df

    def prepare_reviews(self, s):
        ''' преобразование отзывов в список '''
        l = s[2:-2].replace('], [','|').split('|')
        v0 = l[0].split(',')
        v1 = l[1].split(',')
        
        return [v0, v1] 

    def encoding(self, df):
        # ################### 3. Encoding ############################################################## 

        # Cuisine Style
        df.Cuisine_Style = df.Cuisine_Style.str[2:-2].str.split(',')

        # Price Range
        df.Price_Range = df.Price_Range.apply(lambda x: len(str(x)))

        # df['Reviews_Len'] = df.Reviews.apply(lambda x: len(x.strip()))
        # df['Reviews_Words_Num'] = df.Reviews.apply(lambda x: len(x.strip().split(' ')))
        # Преобразование отзвово в список
        df.Reviews = df.Reviews.map(lambda x: self.prepare_reviews(str(x)))

        return df
    
    
    def make_feuture(self, df):
        # ################### 4. Feature Engineering ####################################################
        # тут ваш код не генерацию новых фитчей
        # ....

        # Restaurant_id  надо сделать признак сетевой network
        tmp_dict = df.Restaurant_id.value_counts().to_dict()
        df['Network_size'] = df['Restaurant_id'].map(tmp_dict)
        df['Network'] = df['Network_size'].apply(lambda x: 0 if (x == 1) else 1)


        #####

        population = {'London': 10979, 'Paris': 11020, 'Madrid': 6026, 'Barcelona': 4588,
                        'Berlin': 6177, 'Milan': 4907, 'Rome': 3900, 'Prague': 1308,
                        'Lisbon': 2942, 'Vienna': 2300, 'Amsterdam': 2400, 'Brussels': 1831,
                        'Hamburg': 1841, 'Munich': 1471, 'Lyon': 1748, 'Stockholm': 2352,
                        'Budapest': 2965, 'Warsaw': 3100, 'Dublin': 1347,
                        'Copenhagen': 1308, 'Athens': 3168, 'Edinburgh': 513,
                        'Zurich': 1334, 'Oporto': 1313, 'Geneva': 496, 'Krakow': 1200,
                        'Oslo': 1558, 'Helsinki': 1299, 'Bratislava': 700,
                        'Luxembourg': 626, 'Ljubljana': 508}
        df['Population'] = df.apply(lambda row: population[row['City']], axis=1)        
        
        # City: Город
        tmp_dict = df.City.value_counts().to_dict()
        df['Restaurant_num'] = df['City'].map(tmp_dict)
        df['Restaurant_on_people'] = df.Restaurant_num / df.Population

        # Cuisine Style
        df['Cuisine_Style_Num'] = df.Cuisine_Style.str.len()

        # Ranking: Ранг ресторана относительно других ресторанов в этом городе
        df['Ranking_city'] = df.Ranking / df.City.map(df.groupby(['City'])['Ranking'].max())
        
        # Reviews: 2 последних отзыва и даты этих отзывов
        df['Reviews_Dates'] = df.Reviews.apply(lambda x: x[1])
        df['Reviews_Date1'] = df.Reviews_Dates.apply(lambda x: x[0])
        df['Reviews_Date2'] = df.Reviews_Dates.apply(lambda x: x[-1])
        df['Reviews_Date1'] = pd.to_datetime(df['Reviews_Date1'], errors='coerce')
        df['Reviews_Date2'] = pd.to_datetime(df['Reviews_Date2'], errors='coerce')
        dmax = df.Reviews_Date2.max()
        dmin = df.Reviews_Date1.min()
        df['Reviews_Days_Delta_Min'] = (dmax - df.Reviews_Date2).dt.days
        df['Reviews_Days_Delta_Min'].fillna(0)
        df['Reviews_Days_Delta_Max'] = (dmax - df.Reviews_Date1).dt.days
        df.Reviews_Days_Delta_Max.fillna(df.Reviews_Days_Delta_Max.mean(), inplace=True)
        df.Reviews_Days_Delta_Min.fillna(df.Reviews_Days_Delta_Min.mean(), inplace=True)
        df['Reviews_Days_Delta'] = df.Reviews_Days_Delta_Max - df.Reviews_Days_Delta_Min
        df.drop(['Reviews_Date1', 'Reviews_Date2'], axis = 1, inplace=True)

        
        # URL_TA: страница ресторана на 'www.tripadvisor.com'
        # ID_TA: ID ресторана в TripAdvisor
        # Rating: Рейтинг ресторана

        return df

    def make_dammies(self, df):
        df = pd.get_dummies(df, columns=[ 'City',], dummy_na=True)
        df['Price_Range_num'] = df.Price_Range
        df = pd.get_dummies(df, columns=[ 'Price_Range'], dummy_na=False)

        return df

    
    def clean(self, df):
        # ################### 5. Clean #################################################### 
        # убираем не нужные для модели признаки
        df.drop(['Restaurant_id','ID_TA',], axis = 1, inplace=True)

        # убираем признаки которые еще не успели обработать, 
        # модель на признаках с dtypes "object" обучаться не будет, просто выберим их и удалим
        object_columns = [s for s in df.columns if df[s].dtypes == 'object' or df[s].dtypes == 'timedelta64' or df[s].dtypes == 'datetime64']
        df.drop(object_columns, axis = 1, inplace=True)

        return df
    
    def get_data(self):
        return self.df

