import numpy as np

# my_secret = [x for x in range(1, 301, 7) if x%10 == 7 or x%10 == 1]

# arr = np.array([my_secret, [x/2 for x in my_secret], [x-100 for x in my_secret]])

# print(arr)

# # С помощью каких вариантов кода можно создать массив, среднее арифметическое всех элементов главной диагонали которого равно 1?
# print(np.ones(5))
# # print(np.ones(5,5))
# print(np.ones((5,5)))
# print(np.eye(5))
# print(np.full((5,5), 1))
# print(np.array([[1,2,3,4,5], [5,1,2,3,4], [4,5,1,2,3], [3,4,5,1,2], [2,3,4,5,1]]))

# [[1, 1, 1],
#  [0, 2, 2],
#  [2, 4, 1]]
# С помощью каких вариантов кода НЕВОЗМОЖНО создать массив, представленный в примере выше?
# print(np.random.randint(0, 4, (3, 3)))
# print(np.random.randint(0, 5, (3, 3)))
# print(np.random.randint(0, 6, (3, 3)))
# print(np.random.randint(0, 5, 3))

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

print(big_secret)
# Чему равна сумма элементов последнего столбца массива? Ответ округлите до двух цифр после запятой:
# print(big_secret[4:,0:][0].sum())
# print(round(big_secret[0:,-1:].sum(), 2))
# Выделите из каждой строки массива big_secret первые 5 элементов. 
# Чему равна сумма элементов главной диагонали получившейся матрицы? Округлите ответ до двух цифр после запятой:
# a = big_secret[0:,0:5]
# b = np.eye(5) 
# c = a*b
# print(a)
# print(b)
# print(round(c.sum(), 2))
# Выделите из каждой строки массива big_secret последние 5 элементов. 
# Чему равно произведение элементов главной диагонали получившейся матрицы? Введите полученный результат без изменений и округлений.
# a = big_secret[0:,-5:]
# print(a)
# print(a.diagonal().prod())

# Замените на 1 все элементы, у которых оба индекса нечётные, и на -1 все элементы, у которых оба индекса чётные.
for r in range(np.shape(big_secret)[0]):
    for c in range(np.shape(big_secret)[1]):
        if r % 2 == 0 and c % 2 == 0:
            big_secret[r,c] = -1
        elif r % 2 == 1 and c % 2 == 1:
            big_secret[r,c] = 1

print(big_secret)

# Выделите из каждой строки обновлённого массива big_secret первые 5 элементов. 
# Чему равна сумма элементов главной диагонали получившейся матрицы? 
# Введите полученный ответ без изменений и округлений.
# a = big_secret[0:,0:5]
# print(a)
# print(a.diagonal())
# print(a.diagonal().sum())

# Выделите из каждой строки обновлённого массива big_secret последние 5 элементов. 
# Чему равно произведение элементов главной диагонали получившейся матрицы? 
# Введите полученный результат без изменений и округлений.
a = big_secret[0:,-5:]
print(a)
print(a.diagonal())
print(a.diagonal().prod())

        
