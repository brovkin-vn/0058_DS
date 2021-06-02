import pandas as pd
import numpy as np


# df = pd.read_csv('./module_3_test/train.csv', encoding='ISO-8859-1', low_memory=False)
# # df = df.fillna(0)
# df = np.sqrt(df.balance_due[df.balance_due > 0])
# print(np.median(df) - np.mean(df))

vis_data = pd.read_csv("./module_3_test/train.csv", encoding = 'ISO-8859-1', low_memory = False)
#  


from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(3)
poly_features = pf.fit_transform(vis_data[['balance_due', 'payment_amount']])
 # 
priznaki = poly_features.mean(axis=0)
print(priznaki)
print(priznaki.max())
