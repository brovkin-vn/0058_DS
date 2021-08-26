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

# если оценка 6 то 1 иначе 0
print((df.quality >= 6).astype(int))

X = df.drop('quality', axis=1)
y = df.quality

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=42)

log_reg = LogisticRegression()

log_reg.fit(X_train, y_train)

f1_log_reg = f1_score(y_test, log_reg.predict(X_test), average='weighted')

print(f"F1 для логистической регресии = {np.round(f1_log_reg, 3)}")

