# Загрузите датасет digits с помощью функции load_digits из sklearn.datasets 
# и подготовьте матрицу признаков  и ответы на обучающей выборке  
# (вам потребуются поля data и target в объекте, который возвращает load_digits). 

# 2Информацию о датасете вы можете получить,
#  обратившись к полю DESCR у возвращаемого объекта load_digits.
#  Нам предстоит решать задачу классификации изображений с цифрами по численным признакам.

# 3Для оценки качества мы будем использовать cross_val_score 
# из sklearn.model_selection с параметром .
#  Эта функция реализует k-fold cross validation c  равным значению параметра . 
# Предлагается использовать , чтобы
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score

digits = load_digits(as_frame=True)
X = digits.data
y = digits.target

# dtc_rand = DecisionTreeClassifier()
# print(cross_val_score(dtc_rand, X, y, cv=10, n_jobs=-1).mean())
# # bagging_trees_rand = BaggingClassifier(dtc_rand, n_estimators=100, max_features=int(np.sqrt(X.shape[1])))
# bagging_trees_rand = BaggingClassifier(dtc_rand, n_estimators=100)

# print(cross_val_score(bagging_trees_rand, X, y, cv=10, n_jobs=-1).mean())

random_tree = DecisionTreeClassifier(max_features=int(np.sqrt(X.shape[1])), max_depth=30, random_state=True)
# random_tree = DecisionTreeClassifier(max_depth=30)
print(cross_val_score(random_tree, X, y, cv=10, n_jobs=-1).mean())


bagging_random_trees = BaggingClassifier(random_tree, n_estimators=100)
print(cross_val_score(bagging_random_trees, X, y, cv=10, n_jobs=-1).mean())
