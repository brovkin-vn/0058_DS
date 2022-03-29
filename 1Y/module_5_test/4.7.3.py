import pandas as pd
import numpy as np

data = pd.read_csv('./module_5_test/glass.csv')
print(len(data['Type'].unique()))

X = data[list(set(data.columns) - set(['Type']))].values
y = data['Type'].values

#  воспользуемся k-fold валидацией на десяти разбиениях и обучим модель:
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, KFold
model=KNeighborsClassifier(n_neighbors=3)
kf = KFold(n_splits=10, shuffle=False)
scores = cross_val_score(model, X, y, cv=kf, scoring="accuracy")
print(round(scores.mean(), 2))