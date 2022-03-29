import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

myData = pd.read_csv('mycar.csv')

X = myData.iloc[:,:-1].values
Y = myData.iloc[:,1].values

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.3)

from sklearn.linear_model import LinearRegression

myModel = LinearRegression() #Обозначаем, что наша модель - линейная регрессия
myModel.fit(X_train,Y_train) #обучаем модель на обучающих данных

y_pred = myModel.predict(X_test)
y_pred