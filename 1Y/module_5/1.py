import pandas as pd

df = pd.read_csv('./module_5/,min_train.csv')
# df.info()
# print(df.count())

import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_selection import f_classif, mutual_info_classif
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


from sklearn.metrics import confusion_matrix
from sklearn.metrics import auc, roc_auc_score, roc_curve

# df.info()
# print(df.isnull().sum())
# print(df['education'].value_counts())
df['education'] = df['education'].fillna('NONE')
# print(df.isnull().sum())

tmp = df['education'].value_counts().to_dict()
print(tmp)
for i, k in enumerate(tmp):
    tmp[k] = i
    print(i, k)
print(tmp)
df['education'] = df['education'].map(tmp)
print(df['education'].value_counts())

bin_cols = ['sex','car','car_type','good_work','foreign_passport']
cat_cols = ['education','home_address','work_address']
num_cols = ['age','decline_app_cnt','bki_request_cnt','income']

X_cat = OneHotEncoder(sparse = False).fit_transform(df[cat_cols].values)

# print(X_cat.shape)
