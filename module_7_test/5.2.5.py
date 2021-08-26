
# Обучите решающее дерево для регрессии на предложенных данных, 
# размер тестовой выборки возьмите за 0.3, random_state = 42 для разбиения и дерева. 
# Вычислите RMSE, округлите до двух знаков после точки-разделителя.

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, mean_squared_error
RANDOM_SEED = 42
train = pd.read_csv('module_7_test/petrol_consumption.csv')
y = train['Petrol_Consumption']
X = train.drop(columns=['Petrol_Consumption'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_SEED)
reg_tree = DecisionTreeRegressor(random_state=RANDOM_SEED)
reg_tree.fit(X_train, y_train)

y_predict = reg_tree.predict(X_test)

# Вычислите RMSE, округлите до двух знаков после точки-разделителя.
rmse = np.sqrt(mean_squared_error(y_test, y_predict))
print(round(rmse, 2))
# Какова глубина дерева?
print(reg_tree.get_depth())
