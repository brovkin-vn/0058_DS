import pandas as pd 
import numpy as np 
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression # наша модель для классификации
from sklearn.preprocessing import RobustScaler
df = pd.read_csv('train_mobile.csv', sep=';')
# Удаляем лишние признаки
df2 = df.drop(['blue', 'clock_speed','dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 
'pc', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'wifi'], axis=1)

df2.info()



# # удаляем пропуски в данных
# flats2.dropna(inplace=True)
# # логарифмируем целевой признак
# flats2['price_doc'] = flats2['price_doc'].apply(lambda w: np.log(w + 1))
# готовим данные к обучению
X = df2.iloc[:, :-1]
Y = df2.iloc[:, -1]
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=31)
X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size = 0.2, random_state=31)
model = LogisticRegression()
model.fit(X_train, Y_train)
# Готово! Теперь осталось только вычислить необходимые метрики:

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

Y_predicted = model.predict(X_val)
print(round(precision_score(Y_val,Y_predicted), 4))
