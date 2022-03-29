import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Попробуйте построить модель, предсказывающую пол обладателя записи голоса.
# Для этого:
# Разделите выборку на обучающую и тренировочную с параметрами test_size=0.3, random_state=42.
# Нормализуйте признаки с помощью функции StandardScaler(). Учитывайте, что нормализация тестовой выборки производится по среднему и отклонению тренировочной, которую мы считаем репрезентативной относительно генеральной совокупности.
# Обучите модель логистической регрессии на подготовленных данных.
#  Пояснение
# Тестовые данные не должны влиять на параметры нормализации. 
# Нужно использовать SCALER.TRANSFORM вместо SCALER.FIT_TRANSFORM, 
# чтобы применять параметры нормализации, рассчитанные для тренировочных данных. 
# Иначе данные в трейне и в тесте будут нормализованы по - разному.

data = pd.read_csv('./module_5_test/voiceDataSet.csv')
from sklearn import metrics
data = data.replace('male', 1)
data = data.replace('female',0)
X = data.drop('label', axis = 1)
Y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# lr = LogisticRegression(max_iter=1000)
# lr.fit(X_train,Y_train)
# y_pred = lr.predict_proba(X_test)[:,1]

# sklearn.metrics.accuracy_score(y_true, y_pred, *, normalize=True, sample_weight=None)
# y_true � ������ ������ - ��� Y_test

from sklearn.metrics import accuracy_score

lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(np.round(accuracy, 3))