import pandas as pd
import numpy as np
import sklearn 
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score



df = pd.read_csv('module_7_test/winequality-red.csv', sep=';')
df.info()

df.quality = (df.quality >= 6).astype(int)

df.info()

X = df.drop('quality', axis=1)
y = df.quality

# y = df['quality']
# X = df.drop(columns=['quality'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=42)

# Решающий лес
dtc = DecisionTreeClassifier(random_state=42,
                             max_depth=10).fit(X_train, y_train)
y_pred = dtc.predict(X_test)
f1 = f1_score(y_pred, y_test)
print(f1)
# print(f'{f1_score(y_pred, y_test):.3f}')

# Бэггинг
# обученная модель
clf = BaggingClassifier(base_estimator = dtc,
                        n_estimators=1500,
                        random_state=42).fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f'{f1_score(y_pred, y_test):.3f}')


# новая модель
clf = BaggingClassifier(base_estimator = DecisionTreeClassifier(),
                        n_estimators=1500,
                        random_state=42).fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f'{f1_score(y_pred, y_test):.3f}')