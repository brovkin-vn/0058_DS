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

# first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
# second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
# third_line = [x**2 for x in range(51)]

# big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

# print(big_secret)
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
# for r in range(np.shape(big_secret)[0]):
#     for c in range(np.shape(big_secret)[1]):
#         if r % 2 == 0 and c % 2 == 0:
#             big_secret[r,c] = -1
#         elif r % 2 == 1 and c % 2 == 1:
#             big_secret[r,c] = 1

# print(big_secret)

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
# a = big_secret[0:,-5:]
# print(a)
# print(a.diagonal())
# print(a.diagonal().prod())


# Рассмотрим примеры использования индексов при работе с одномерным массивом.
# my_array = np.array([x for x in range(10)])
# print(my_array)
# print(my_array[5])
# print(my_array[-1])
# print(my_array[3:6])
# print(my_array[1:8:3])

# У нас есть два массива: найдём их сумму, разность, произведение, частное и умножим один из массивов на число:
# a = np.array([3,6,9])
# b = np.array([12,15,18])

# result1 = a+b
# result2 = b-a
# result3 = a*b
# result4 = a/b
# result5 = a*2
# print('Сумма: {}\nРазность: {}\nПроизведение: {}\nЧастное: {}\nУмножение на число: {}'.format(result1, result2, result3, result4, result5))

# Транспонирование
# my_array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(my_array)
# print(my_array.T)

# Изменение размерности
# my_array = np.random.randint(0, 10, 20)
# print(my_array)
# print(my_array.reshape((4,5)))

# Для преобразования многомерного массива в одномерный используется метод flatten:
# my_array = np.array([[1,2,3], [11,22,33], [111,222,333]])
# print(my_array)
# print(my_array.flatten())

# Сравнения
# my_array = np.random.randint(0, 10, (3,4))
# print(my_array)
# print(my_array < 5)
# print(my_array[my_array < 5])

# Маска
# mask = np.array([1, 0, 1, 0], dtype=bool)
# print(mask)
# print(my_array[:, mask])

# Сортировка
# my_array = np.random.randint(0, 10, (4, 6))
# print(my_array)
# print(np.sort(my_array, axis=1))
# print(np.sort(my_array, axis=0))

# first = [x**(1/2) for x in range(100)]
# second = [x**(1/3) for x in range(100, 200)]
# third = [x/y for x in range(200,300,2) for y in [3,5]]

# great_secret = np.array([first, second, third]).T
# print(great_secret)

# Чему равна сумма косинусов элементов первой строки массива great_secret? Ответ округлите до двух знаков после запятой.
# a = great_secret[0:1]
# print(a)
# print(round(np.cos(a).sum(), 2))

# Чему равна сумма элементов массива great_secret, значение которых больше 50?
# a = great_secret[great_secret > 50]
# print(a)
# print(a.sum())

# Переведите массив great_secret в одномерную форму. 
# Какое значение в получившемся массиве имеет элемент с индексом 150? 
# Скопируйте ответ из Jupyter Notebook без изменений.
# a = great_secret.flatten()
# print(a)
# print(a[150])

# Отсортируйте значения столбцов массива great_secret по возрастанию. 
# Чему равна сумма элементов последней строки отсортированного массива? 
# Ответ округлите до двух цифр после запятой.Отсортируйте значения столбцов массива great_secret по возрастанию.
#  Чему равна сумма элементов последней строки отсортированного массива? Ответ округлите до двух цифр после запятой.
# a = np.sort(great_secret, axis = 0)
# b = a[-1:]
# print(a)
# print(round(b.sum(),2))

students = np.array([
    [1, 135, 34, 4],
    [2, 160, 43, 5],
    [3, 163, 40, 4.3],
    [4, 147, 44, 5],
    [5, 138, 41, 4.7],
    [6, 149, 54, 3.9],
    [7, 136, 39, 4.2],
    [8, 154, 48, 4.9],
    [9, 137, 35, 3.7],
    [10, 165, 60, 4.6]
])

# print(students)

# mean = np.mean(students[:,-1])
# print(mean)
# median = np.median(students[:,-1])
# print(median)
# sort = np.sort(students[:,-1])
# print((sort[4]+sort[5])/2)

# # Чему равно медианное значение массы тела школьников?
# print(np.median(students[:,-2]))
# print(round(np.mean(students[:,-2]) - np.median(students[:,-2]), 1))

# corr = np.corrcoef(students[:,1], students[:,2])
# print(corr)

# Между какой парой признаков в массиве students наблюдается минимальная корреляция, из предложенных вариантов?
# # между ростом и массой тела
# print(np.corrcoef(students[:,1], students[:,2]))
# # между ростом и успеваемостью
# print(np.corrcoef(students[:,1], students[:,3]))
# # между массой тела и успеваемостью
# print(np.corrcoef(students[:,2], students[:,3]))

# std = np.std(students[:,1])
# print(std)

# Используя имеющийся набор данных о школьниках, найдите, чему равно стандартное отклонение их средних баллов.
# std = np.std(students[:,3])
# print(std)

# Посчитайте, чему равна дисперсия значений веса школьников.
# print(np.var(students[:,2]))

# my_array = np.array([[1,2,3,4,5],
#                      [6,7,8,9,10],
#                      [11,12,13,14,15],
#                      [16,17,18,19,20],
#                      [21,22,23,24,25]])

# print(my_array)                
# # извлечь из него центральный фрагмент размером 3 х 3     
# print(my_array[1:4,1:4])     
# # Создайте массив my_sin, состоящий из синусов элементов массива my_array. Посчитайте, чему равна сумма элементов полученного массива. Ответ округлите до трёх цифр после запятой.                
# my_sin = np.sin(my_array)
# print(round(my_sin.sum() ,3))

# my_sin[1:4,1:4] = 1
# print(round(my_sin.sum() ,3))


# Преобразуйте первые четыре столбца массива my_sin в массив из 10 строк и 2 столбцов. 
# Чему равна сумма элементов первого столбца получившегося массива? 
# Ответ округлите до трёх заков после точки-разделителя. 
# Используйте преобразованный в предыдущем задании массив my_sin.


# a = my_sin[:,0:4]
# b = a.reshape((10,2))
# c = b[:, 0]
# print(a)
# print(b)
# print(round(c.sum(), 3))

# Создайте массив bigdata, содержащий квадраты всех нечётных чисел в диапазоне от 100 до 1000.
bigdata = np.array([x**2 for x in range(101, 1000, 2)])
print(bigdata)
# Чему равна медиана массива bigdata?
print(bigdata.shape)
print(np.median(bigdata))
# Чему равно стандартное отклонение для массива bigdata? Ответ округлите до целых:
print(round(np.std(bigdata)))
# Чему равен коэффициент корреляции между элементами массива bigdata с чётными и нечётными индексами?
print(np.corrcoef(bigdata[0::2], bigdata[1::2]))


