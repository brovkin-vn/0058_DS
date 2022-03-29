import pandas as pd
import numpy as np

def removeOutliers(data, col):
    Q3 = np.quantile(data[col], 0.75)
    Q1 = np.quantile(data[col], 0.25)
    IQR = Q3 - Q1
     
    # print("IQR value for column %s is: %s" % (col, IQR))
    global outlier_free_list
    global filtered_data
     
    lower_range = Q1 - 1.5 * IQR
    upper_range = Q3 + 1.5 * IQR
    outlier_free_list = [x for x in data[col] if (
        (x >= lower_range) & (x <= upper_range))]
    filtered_data = data.loc[data[col].isin(outlier_free_list)]
    # print(col)
    # print(filtered_data.info())
    # print("\n")

df = pd.read_csv('./module_5_test/heart_fin1.csv',sep=';')

for col in df.columns[:-1]:
    removeOutliers(df, col)
    df = filtered_data

X = df.iloc[:, :-1]
Y = df.iloc[:, -1]


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=5)
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

from sklearn.metrics import  roc_auc_score
roc_auc = roc_auc_score(y_test, y_pred)
print(roc_auc)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, KFold
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
roc_auc = roc_auc_score(y_test, y_pred)
print(roc_auc)

# kf = KFold(n_splits=10, shuffle=False)
# scores = cross_val_score(model, X_train, y_train, cv=kf, scoring="accuracy")
# print(round(scores.mean(), 2))

