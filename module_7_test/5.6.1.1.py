import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestRegressor 


weather = pd.read_csv("module_7_test/temps_extended.csv")

y = weather['actual']
X = weather.drop(['actual','weekday','month','day','year'],axis =1)
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3, random_state=42)


best_params = {'bootstrap': True,
 'max_depth': 10,
 'max_features': 'sqrt',
 'min_samples_leaf': 2,
 'min_samples_split': 5,
 'n_estimators': 1000}

rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)

y_pred_st = rf.predict(X_test)
mse_st = mean_squared_error(y_test, y_pred_st)

# Оптимальные гиперпаметры:
# best_params = rf_random.best_params_

rf_opt = RandomForestRegressor(random_state=42).set_params(**best_params)

rf_opt.fit(X_train, y_train)

y_pred_opt = rf_opt.predict(X_test)
mse_opt = mean_squared_error(y_test, y_pred_opt)

print(f"Улучшение MSE = {np.round(mse_st - mse_opt, 1)}")

# {'bootstrap': True,
#  'max_depth': 10,
#  'max_features': 'sqrt',
#  'min_samples_leaf': 2,
#  'min_samples_split': 5,
#  'n_estimators': 1000}