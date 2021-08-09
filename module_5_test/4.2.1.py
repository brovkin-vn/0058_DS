import pandas as pd
from sklearn.model_selection import train_test_split
vis_data = pd.read_csv("./module_5_test/train.csv", encoding = 'ISO-8859-1', low_memory = False)
# Загрузите данные train.csv, разделите выборку на обучающую и тестовую части в соотношении 
# 70% на 30% без перемешивания.
# Найдите среднее значение для признака payment_amount и запишите его в 
# переменную result. Обратите внимание, что среднее нужно считать по тестовой выборке.
# Напишите ваш код ниже
from sklearn.model_selection import train_test_split
train, test = train_test_split(vis_data, test_size=0.30, shuffle=False)
result =  test['payment_amount'].mean()
