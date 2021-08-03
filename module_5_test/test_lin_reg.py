import pandas as pd 
import numpy as np 
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import RobustScaler
flats = pd.read_csv('module_5_test/data_flats.csv', sep=';')
# Удаляем лишние признаки
flats2 = flats.drop(['id', 'life_sq','kindergarten_km', 'park_km', 'kremlin_km', 'preschool_education_centers_raion'], axis=1)
# удаляем пропуски в данных
flats2.dropna(inplace=True)
# логарифмируем целевой признак
flats2['price_doc'] = flats2['price_doc'].apply(lambda w: np.log(w + 1))
# готовим данные к обучению
X = flats2.iloc[:, :-1]
Y = flats2.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=77)
# Нормализация обучающей и тестовой выборки
scaler = RobustScaler()
X_train_transformed = scaler.fit_transform(X_train)
X_test_transformed = scaler.transform(X_test)
# обучаем регрессию
lrg = LinearRegression()
lrg.fit(X_train_transformed, y_train)
# строим предсказание
y_pred = lrg.predict(X_test_transformed)
# проверяем метрику
mse = metrics.mean_squared_error(
    np.exp(y_test) - 1, np.exp(y_pred) - 1)
print(round(mse))