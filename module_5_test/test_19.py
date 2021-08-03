import pandas as pd               # библиотека для работы с таблицами
import numpy as np                # библиотека для работы с матрицами

# Рассмотрим очень простой пример. Предположим, что у нас есть показатели уровня счастья для пяти человек:
y_happy = [4,20,110,15,23]
# Допустим, у нас есть показатели счастья для этих же пяти человек, но предсказанные некоторым алгоритмом:
y_happy_pred = [5,15,100,9,21]
# Давайте вычислим метрики для этих данных!
from sklearn import metrics  # подгружаем метрики

#Вычисляем MAE:
MAE = metrics.mean_absolute_error(y_happy, y_happy_pred)
print(MAE)
# Вычисляем MSE:
MSE = metrics.mean_squared_error(y_happy, y_happy_pred)
print(MSE)
#Вычисляем коэффициент детерминации:
R_2 = metrics.r2_score(y_happy, y_happy_pred)
print(R_2)



y = [	2,	3,	-1,	4]
y_ = [	1,	3,	2,	5]
# Вычисляем MSE:
MSE = metrics.mean_squared_error(y, y_)
print(MSE)

# Истинное значение	2	3	-1	4
# Предсказанное значение	1	3	2	5
y = [	2,	3,	-1,	4]
y_ = [	1,	3,	2,	5]
#Вычисляем коэффициент детерминации:
R_2 = metrics.r2_score(y, y_)
print(R_2)
import seaborn as sns
