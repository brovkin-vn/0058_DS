import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
vis_data = pd.read_csv("./module_5_test/train.csv", encoding = 'ISO-8859-1', low_memory = False)
# Загрузите данные train.csv, 
# оставьте в данных только признаки  'fine_amount', 'state_fee', 'late_fee', 'discount_amount', 'balance_due', 
# затем избавьтесь от пропусков. Целевой переменной будет 'balance_due', 
# разделите данные на обучающую и тестовую выборки в соотношении 70% / 30% без перемешивания. 
# Обучите линейную регрессию из scikit-learn и запишите в переменную result значение метрики RMSE
# на тестовой выборке. RMSE означает Rooted Mean Squared Error. Rooted означает, что из значения метрики был взят корень.
# Напишите ваш код ниже
# оставьте в данных только признаки  'fine_amount', 'state_fee', 'late_fee', 'discount_amount', 'balance_due', 
df = vis_data[['fine_amount', 'state_fee', 'late_fee', 'discount_amount', 'balance_due']]

# затем избавьтесь от пропусков. Целевой переменной будет 'balance_due', 
df.dropna(axis = 0, inplace=True)

# готовим данные к обучению
X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

# разделите данные на обучающую и тестовую выборки в соотношении 70% / 30% без перемешивания. 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, shuffle=False)

# Обучите линейную регрессию из scikit-learn и запишите в переменную result значение метрики RMSE
from sklearn.linear_model import LinearRegression # наша модель для классификации
model = LinearRegression()
model.fit(X_train, Y_train)

import numpy as np
import math
Y_pred = model.predict(X_test)
result = np.sqrt(mean_squared_error(Y_test, Y_pred))
print(result)







