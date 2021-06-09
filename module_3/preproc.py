import pandas as pd
import numpy as np
import re
import datetime
import time

class Preproc():

    def __init__(self, df):
        self.df = df.copy()
        self.prepare()
        self.fill_nan()
        self.encoding()
        self.make_feuture()
        self.clean()

    def prepare(self):
        # ################### 1. Предобработка ############################################################## 
        # убираем не нужные для модели признаки
        self.df.drop(['Restaurant_id','ID_TA',], axis = 1, inplace=True)
    
    
    def fill_nan(self):
        # ################### 2. NAN ############################################################## 
        # Далее заполняем пропуски, вы можете попробовать заполнением средним или средним по городу и тд...
        self.df['Number of Reviews'].fillna(round(self.df['Number of Reviews'].mean()), inplace=True)
        self.df['Number_of_Reviews_isNAN'] = pd.isna(self.df['Number of Reviews']).astype('uint8')
        
        # Cuisine Style
        self.df['Cuisine_Style_isNAN'] = pd.isna(self.df['Cuisine Style']).astype('uint8')
        self.df['Cuisine Style'].fillna('other', inplace=True)

        self.df['Price Range_isNAN'] = pd.isna(self.df['Price Range']).astype('uint8')
        self.df['Price Range'].fillna('$$ - $$$', inplace=True)
    
        self.df['Reviewse_isNAN'] = pd.isna(self.df['Reviews']).astype('uint8')
        self.df['Reviews'].fillna('[[], []]', inplace=True)
    
    def encoding(self):
        # ################### 3. Encoding ############################################################## 

        # Cuisine Style
        self.df['Cuisine Style'] = self.df['Cuisine Style'].str[2:-2].str.split(',')
        self.df['Cuisine Style Num'] = self.df['Cuisine Style'].str.len()

        # Ranking
        self.df['Ranking_city'] = self.df['Ranking'] / self.df['City'].map(self.df.groupby(['City'])['Ranking'].max())
        # ....

        # для One-Hot Encoding в pandas есть готовая функция - get_dummies. Особенно радует параметр dummy_na
        self.df = pd.get_dummies(self.df, columns=[ 'City',], dummy_na=True)
        # тут ваш код не Encoding фитчей
        # Price Range
        self.df['Price Range'] = self.df['Price Range'].apply(lambda x: len(str(x)))
        self.df['Price_Range'] = self.df['Price Range']
        self.df = pd.get_dummies(self.df, columns=[ 'Price Range'], dummy_na=False)

        pass
    
    
    def make_feuture(self):
        # ################### 4. Feature Engineering ####################################################
        # тут ваш код не генерацию новых фитчей
        # ....
        pass
    
    
    def clean(self):
        # ################### 5. Clean #################################################### 
        # убираем признаки которые еще не успели обработать, 
        # модель на признаках с dtypes "object" обучаться не будет, просто выберим их и удалим
        object_columns = [s for s in self.df.columns if self.df[s].dtypes == 'object']
        self.df.drop(object_columns, axis = 1, inplace=True)
    
    def get_data(self):
        return self.df

