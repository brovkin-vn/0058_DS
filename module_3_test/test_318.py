import pandas as pd
import numpy as np


# df = pd.read_csv('./module_3_test/train.csv', encoding='ISO-8859-1', low_memory=False)
# # df = df.fillna(0)
# df = np.sqrt(df.balance_due[df.balance_due > 0])
# print(np.median(df) - np.mean(df))

vis_data = pd.read_csv("./module_3_test/train.csv", encoding = 'ISO-8859-1', low_memory = False)
vis_data.balance_due.dropna()
vis_data = vis_data.loc[vis_data.balance_due > 0]
def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))[0]

# удаление выбросов
o = outliers_iqr(vis_data.balance_due)
print(o)
data = vis_data.loc[~vis_data['balance_due'].isin(o)]
print(data.balance_due.min())
print(data.balance_due.max())
print(data.balance_due.max() - data.balance_due.min())


#  


# from sklearn.preprocessing import PolynomialFeatures
# pf = PolynomialFeatures(3)
# poly_features = pf.fit_transform(vis_data[['balance_due', 'payment_amount']])
#  # 
# priznaki = poly_features.mean(axis=0)
# print(priznaki)
# print(priznaki.max())

print('OK')