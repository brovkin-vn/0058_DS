# Задание 3B2.2
# 1 point possible (graded)
# Загрузите встроенный в библиотеку sklearn датасет про ирисы с помощью функции load_iris. 
# Обучите модель логистической регрессии (random_state=50, размер тестовой выборки 0.3) 
# и укажите полученное значение метрики .
# Ответ округлите до сотых. Пример ввода: 5.55.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
iris = load_iris()
Y = iris.target
X = iris.data
X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.3, random_state=50)
# model = LogisticRegression(solver='liblinear')  
model = LogisticRegression()  
# (со стоящим по умолчанию солвером lbfgs обучение расходится)
model.fit(X_train, Y_train)
Y_predicted = model.predict(X_val)
print(accuracy_score(Y_val, Y_predicted))