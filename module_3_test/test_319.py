import numpy as np
import pandas as pd

vis_data = pd.read_csv("./module_3_test/train.csv", 
                       encoding = 'ISO-8859-1', 
                       low_memory = False)
vis_data = vis_data.drop(['violation_zip_code', 'clean_up_cost'], axis=1)
latlons = pd.read_csv("./module_3_test/latlons.csv")
vis_data = pd.concat([vis_data, latlons], axis=1)

from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(2)
poly_features = pf.fit_transform(vis_data[['balance_due', 'payment_amount']])
print(poly_features)
print(poly_features.shape)

print(pd.get_dummies(vis_data.state).shape)
datetime_vals = pd.to_datetime(vis_data.payment_date.dropna())
print(datetime_vals.head())

# Загрузите данные train.csv, найдите признак, обозначающий баланс и признак, обозначающий размер платежа (payment_amount). Создайте полиномиальные признаки степени 3. Посчитайте среднее значение для каждого получившегося признака. В качестве ответа укажите индекс признака, который содержит максимальное среднее значение.

priznaki = poly_features.mean(axis=0)
print(priznaki)
print(priznaki.max())

# Загрузите данные train.csv, найдите признак, обозначающий дату, когда был выписан штраф. 
# Найдите, сколько раз штраф был выписан на выходных и запишите это число в качестве ответа.
datetime_vals = pd.to_datetime(vis_data.payment_date.dropna())
dt_issued_date = pd.to_datetime(vis_data.ticket_issued_date)
vis_data['is_weekend'] = dt_issued_date.dt.weekday > 4
vis_data['wd'] = dt_issued_date.dt.weekday
print(vis_data.wd.value_counts())
print(vis_data.is_weekend.value_counts())
