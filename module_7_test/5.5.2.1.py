import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn.ensemble import BaggingClassifier

import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("module_7_test/winequality-red.csv", sep=';')

df.quality = (df.quality >= 6).astype(int)

X = df.drop('quality', axis=1)
y = df.quality

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=42)

log_reg = LogisticRegression()
dec_tree = DecisionTreeClassifier(random_state=42, max_depth=10)

log_reg.fit(X_train, y_train)
dec_tree.fit(X_train, y_train)

f1_log_reg = f1_score(y_test, log_reg.predict(X_test))
f1_dec_tree = f1_score(y_test, dec_tree.predict(X_test))

print(f"F1 для логистической регресии = {np.round(f1_log_reg, 3)}")
print(f"F1 для решающего дерева = {np.round(f1_dec_tree, 3)}")

#F1 для логистической регресии = 0.757
#F1 для решающего дерева = 0.793
# После этого - берем уже обученную модель dec_tree и передаем в бэггинг
#Алгоритм решающего дерева показал лучшее качество, поэтому бэггинг будем использовать для него:

bag_clf = BaggingClassifier(dec_tree, n_estimators=1500, random_state=42)
bag_clf.fit(X_train, y_train)

y_pred = bag_clf.predict(X_test)
f1_bagging = f1_score(y_test, y_pred)

print(f"F1 для бэггинга = {np.round(f1_bagging, 3)}")

#F1 для бэггинга = 0.818