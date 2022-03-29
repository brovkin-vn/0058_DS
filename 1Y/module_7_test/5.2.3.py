# Обучите на предложенных данных решающее дерево. 
# Целевой переменной здесь является переменная Class. 
# Размер тестовой выборки возьмите за 0.2, random_state = 17 для разбиения и дерева. 
# Максимальную глубину дерева примите за 3,
#  максимальное число признаков, по которым ищется лучшее разбиение в дереве — за 2. 
# Какое значение f1-score вы получили? Округлите до трёх знаков после точки-разделителя.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
RANDOM_SEED = 17
train = pd.read_csv('module_7_test/bill_authentication.csv')
y = train['Class']
X = train.drop(columns=['Class'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_SEED)
# clf_tree = DecisionTreeClassifier(max_depth=3, random_state=RANDOM_SEED, max_features = 2)
clf_tree = DecisionTreeClassifier(criterion="gini",max_depth=3, random_state=RANDOM_SEED, max_features = 2)
# clf_tree = DecisionTreeClassifier(criterion="entropy",max_depth=3, random_state=RANDOM_SEED, max_features = 2)
clf_tree.fit(X_train, y_train)
y_predict = clf_tree.predict(X_test)
f1_test = f1_score(y_test, y_predict)

print(round(f1_test, 3))