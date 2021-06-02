import pandas as pd
import numpy as np


df = pd.read_csv('./module_3_test/train.csv', encoding='ISO-8859-1', low_memory=False)
df = df.fillna(0)
# df.info()
data = df.balance_due.values
print(data.shape)
data = data.reshape(-1,1)
print(data.shape)

# Загрузите данные train.csv, найдите признак, обозначающий баланс. Нормализуйте признак с помощью std-нормализации. Проверьте, что вы нашли нужный признак и нормализовали его подходящим методом. Метод для нормализации принимает матрицу, а не массив. В numpy можно превратить массив в матрицу с помощью reshape(). В качестве ответа укажите минимальное значение в получившемся нормализованном признаке. Ответ округлите до 5 знаков после запятой.

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data = scaler.fit_transform(data)
# mode_state = vis_data.state.value_counts().index[0]
# result = vis_data.state.fillna(mode_state)
print(np.min(data))
