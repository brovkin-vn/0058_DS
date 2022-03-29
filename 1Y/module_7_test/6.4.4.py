import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
 
def AdaBoost_scratch(X,y, M=10, learning_rate = 1):
    # инициалиазция служебных переменных
    N = len(y)
    estimator_list, y_predict_list, estimator_error_list, estimator_weight_list, sample_weight_list = [], [],[],[],[]

    # инициализация весов
    sample_weight = np.ones(N) / N
    sample_weight_list.append(sample_weight.copy())

    # цикл по длине М
    for m in range(M):   

        # обучим базовую модель и получим предсказание
        estimator = DecisionTreeClassifier(max_depth = 1, max_leaf_nodes=2)
        estimator.fit(X, y, sample_weight=sample_weight)
        y_predict = estimator.predict(X)

        # Маска для ошибок классификации
        incorrect = (y_predict != y)

        # Оцениваем ошибку
        estimator_error = (sample_weight * incorrect).sum() / sample_weight.sum()
        
        # Вычисляем вес нового алгоритма
        estimator_weight =  learning_rate * np.log((1-estimator_error)/estimator_error)

        # Получаем новые веса объектов
        sample_weight *= np.exp(estimator_weight * incorrect * ((sample_weight > 0) | (estimator_weight < 0)))

        # Сохраяем результаты данной итерации
        estimator_list.append(estimator)
        y_predict_list.append(y_predict.copy())
        estimator_error_list.append(estimator_error.copy())
        estimator_weight_list.append(estimator_weight.copy())
        sample_weight_list.append(sample_weight.copy())

        #Convert to np array for convenience   
        estimator_list = np.asarray(estimator_list)
        y_predict_list = np.asarray(y_predict_list)
        estimator_error_list = np.asarray(estimator_error_list)
        estimator_weight_list = np.asarray(estimator_weight_list)
        sample_weight_list = np.asarray(sample_weight_list)


        #Predictions
        preds = (np.array([np.sign((y_predict_list[:,point] * estimator_weight_list).sum()) for point in range(N)]))
        print('Accuracy = ', (preds == y).sum() / N) 
        


    # Для удобства переведем в numpy.array   
    estimator_list = np.asarray(estimator_list)
    y_predict_list = np.asarray(y_predict_list)
    estimator_error_list = np.asarray(estimator_error_list)
    estimator_weight_list = np.asarray(estimator_weight_list)
    sample_weight_list = np.asarray(sample_weight_list)

    # Получим предсказания
    preds = (np.array([np.sign((y_predict_list[:,point] * estimator_weight_list).sum()) for point in range(N)]))
    print('Accuracy = ', (preds == y).sum() / N) 
    
    return estimator_list, estimator_weight_list, sample_weight_list


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


estimator_list, estimator_weight_list, sample_weight_list  = AdaBoost_scratch(X, y, M=10, learning_rate=0.001)
print(f'estimator_list: {estimator_list}')
print(f'estimator_weight_list: {estimator_weight_list}')
print(f'sample_weight_list: {sample_weight_list}')

accuracy = accuracy_score(y_pred, y_test)
# accuracy = accuracy_score(estimator_list, y_test)
print(f'accuracy: {round(accuracy, 3)}')