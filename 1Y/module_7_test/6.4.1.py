import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
 

df = pd.read_csv('module_7_test/spam7.csv')


df['spam'] = (df.yesno == 'y').astype(int)
df = df.drop(df.columns[[0,7]], axis=1)

X = df.drop('spam', axis=1)
y = df.spam

columns = X.columns
for col in columns:
    for col1 in columns:
        if col != col1 and col+'_'+col1 not in X.columns and col1+'_'+col not in X.columns:
            X[col+'_'+col1] = X[col] * X[col1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

gbs = GradientBoostingClassifier(learning_rate=0.1, n_estimators=100,max_depth=3, min_samples_split=2, min_samples_leaf=1, subsample=1,max_features=None)
gbs.fit(X_train, y_train)
y_pred = gbs.predict(X_test)
accuracy = accuracy_score(y_pred, y_test)
print(f'accuracy: {round(accuracy, 3)}')
feat_importances = pd.Series(gbs.feature_importances_, index=X.columns)
print(feat_importances.sort_values().tail(3))

param_grid = {'learning_rate':[0.00001, 0.0001, 0.001, 0.01, 0.1, 1], 
              'n_estimators':[100, 250, 500, 750, 1000, 1250, 1500, 1750]}
grid = GridSearchCV(gbs, param_grid, scoring = 'accuracy', n_jobs = -1, cv=5)
grid_model = grid.fit(X_train, y_train)
y_pred = grid_model.predict(X_test)

print(f'best_score: {round(grid.best_score_, 3)}')
