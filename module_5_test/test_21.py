from sklearn.model_selection import train_test_split # функция, чтобы разбить данные на трейн и тест
from sklearn.linear_model import LogisticRegression # наша модель для классификации
# Воспользуемся встроенным датасетом, который содержит информацию об опухолях груди:

from sklearn.datasets import load_breast_cancer # подгружаем датасет
breast_cancer = load_breast_cancer()
# Теперь зададим зависимую и независимые переменные:

Y = breast_cancer.target ## Наша целевая переменная, 0 — если рака нет, 1 — если есть 
X = breast_cancer.data # X - признаки, по которым мы будем предсказывать рак 
# Разбиваем выборку на обучающую и тестовую и обучаем нашу модель:

X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size = 0.3)
model = LogisticRegression()
model.fit(X_train, Y_train)
# Готово! Теперь осталось только вычислить необходимые метрики:

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

Y_predicted = model.predict(X_val)
print(Y_predicted)
print(accuracy_score(Y_val,Y_predicted))
print(precision_score(Y_val,Y_predicted))
print(recall_score(Y_val,Y_predicted))
print(f1_score(Y_val,Y_predicted))