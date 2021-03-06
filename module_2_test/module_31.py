import pandas as pd
from math import sqrt

# Для случайной величины  найдите дисперсию  и стандартное отклонение :

# df = pd.DataFrame({
#     'X': [2, 3, 4, 5],
#     'P': [0.1, 0.2, 0.6, 0.1]
# })

# df = pd.DataFrame({
#     'X': [1, 2, 3, 4, 5, 6, 7, 8],
#     'P': [0.05, 0.1, 0.3, 0.25, 0.15, 0.07, 0.05, 0.03]
# })


# from math import sqrt
# # математическое ожидание
# E = (df.X * df.P).sum()
# # дисперсия
# Var = ((df.X - E)**2 * df.P).sum()
# # стандартное отклонение
# sigma = sqrt(Var)
# print(E)
# print(Var)
# print(sigma)


# Фирма производит гвозди. 
# Гвозди продаются в небольших упаковках, в каждую попадает  гвоздей.
# # Ниже представлено распределение вероятностей :
# df = pd.DataFrame({
#     'X': [38, 39, 40, 41, 42, 43],
#     'P': [0.1, 0.1, 0.3, 0.2, 0.2, 0.1]
# })

# # математическое ожидание
# E = (df.X * df.P).sum()
# # дисперсия
# Var = ((df.X - E)**2 * df.P).sum()
# # стандартное отклонение
# sigma = sqrt(Var)
# print(E)
# print(Var)
# print(sigma)
# # Вес одного гвоздя 10 граммов, вес пустой упаковки 20 граммов. 
# # На основании ответов, полученных в первой части, найдите средний вес упаковки с гвоздями и его стандартное отклонение.
# # вес упаковки
# E2 = E*10 + 20
# print(E2)
# # дисперсия упаковках
# Var2 = ((df.X*10 + 20 - E2)**2 * df.P).sum()
# Var2 = Var * 10**2
# print(Var2)
# # Стандартное отколнение
# print(round(sqrt(Var2), 1))


# X и Y — случайные величины со следующими распределениями вероятностей:

dfX = pd.DataFrame({
    'X': [1, 2, 3, 4],
    'P': [0.2, 0.1, 0.4, 0.3]
})

dfY = pd.DataFrame({
    'Y': [-1, 0, 1, 2],
    'P': [0.5, 0.2, 0.1, 0.2]
})

# математическое ожидание
Ex = (dfX.X * dfX.P).sum()
Ey = (dfY.Y * dfY.P).sum()
# дисперсия
VarX = ((dfX.X - Ex)**2 * dfX.P).sum()
VarY = ((dfY.Y - Ey)**2 * dfY.P).sum()
print(f'Ex: {Ex}')
print(f'EY: {Ey}')
print(f'VarX: {VarX}')
print(f'VarY: {VarY}')
# U = 3X + 1, S = 5 - Y
print(f'Eu: {round(Ex*3 + 1, 2)}')
print(f'Es: {5 - Ey}')
print(f'VarU: {round(VarX*3**2, 2)}')
print(f'VarS: {round(VarY, 2)}')
