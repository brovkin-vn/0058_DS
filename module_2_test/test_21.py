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
print(np.random.randint(0, 4, (3, 3)))
print(np.random.randint(0, 5, (3, 3)))
print(np.random.randint(0, 6, (3, 3)))
print(np.random.randint(0, 5, 3))
