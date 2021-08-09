# Постройте модель логистической регрессии при помощи sklearn. 
# Используйте параметры по умолчанию, 
# обучите на всей выборке и посчитайте F1 score.

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, f1_score, accuracy_score, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split

# Реализовать функцию sigmoid
def sigmoid(X, theta):
    return 1. / (1. + np.exp(-X.dot(theta)))

        
# Реализовать функцию, вычисляющую градиент бинарной кросс-энтропии
def calc_binary_cross_entropy_grad(X, y, theta):
    n = X.shape[0]
    grad = 1. / n * X.transpose().dot(sigmoid(X, theta) - y)
    
    return grad

def print_logisitc_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    print(f'acc = {acc:.2f} F1-score = {f1:.2f}')

def gradient_step(theta, theta_grad, alpha):
    return theta - alpha * theta_grad

def optimize(X, y, grad_func, start_theta, alpha, n_iters):
    theta = start_theta.copy()
    
    for i in range(n_iters):
        theta_grad = grad_func(X, y, theta)
        theta = gradient_step(theta, theta_grad, alpha)
    
    return theta

adult = pd.read_csv('./module_5_test/adult.data',
                    names=['age', 'workclass', 'fnlwgt', 'education',
                           'education-num', 'marital-status', 'occupation',
                           'relationship', 'race', 'sex', 'capital-gain',
                           'capital-loss', 'hours-per-week', 'native-country', 'salary'])    

# Избавиться от лишних признаков
adult.drop(['native-country'], axis=1, inplace=True)
# Сконвертировать целевой столбец в бинарные значения
adult['salary'] = (adult['salary'] != ' <=50K').astype('int32')
# Сделать one-hot encoding для некоторых признаков
adult = pd.get_dummies(adult, columns=['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex'])

# Нормализовать нуждающиеся в этом признаки
a_features = adult[['age', 'education-num', 'hours-per-week', 'fnlwgt', 'capital-gain', 'capital-loss']].values
norm_features = (a_features - a_features.mean(axis=0)) / a_features.std(axis=0)
adult.loc[:, ['age', 'education-num', 'hours-per-week', 'fnlwgt', 'capital-gain', 'capital-loss']] = norm_features

# Разбить таблицу данных на матрицы X и y
X = adult[list(set(adult.columns) - set(['salary']))].values
y = adult['salary'].values

# Добавить фиктивный столбец единиц (bias линейной модели)
X = np.hstack([np.ones(X.shape[0])[:, np.newaxis], X])
m = X.shape[1]

# # Разбить выборку на train/valid, оптимизировать theta,
# # сделать предсказания и посчитать ошибку F1-score

# X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2)
# theta = optimize(X_train, y_train, calc_binary_cross_entropy_grad, np.ones(m), 1., 300)
# y_pred = sigmoid(X_valid, theta) > 0.5
# print_logisitc_metrics(y_valid, y_pred)

# Оптимизировать параметр линейной регрессии theta на всех данных
theta = optimize(X, y, calc_binary_cross_entropy_grad, np.ones(m), 1., 300)
# сделать предсказания и посчитать ошибку F1-score
y_pred = sigmoid(X, theta) > 0.5
print_logisitc_metrics(y, y_pred)

# Посчитайте confusion matrix для классификатора из задачи 3.6.1. 
# Для получения матрицы можно воспользоваться методом sklearn.metrics.confusion_matrix(y_true, y_pred), 
# либо посчитать каждый элемент вручную.


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y, y_pred)
print(sum((y == 1)&(y_pred == 1)))
print(cm)

from sklearn.metrics import roc_auc_score
def predict_proba(X):
    return sigmoid(X, theta)

y_pred_proba_pack = predict_proba(X)
roc = roc_auc_score(y, y_pred_proba_pack)
print(roc) 