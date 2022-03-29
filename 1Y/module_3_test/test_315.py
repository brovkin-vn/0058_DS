import numpy as np

A=np.array( [[ 8 , 6 ,11],[ 7 , 5 , 9],[ 6 ,10,  6]])

# print(np.linalg.inv(A))
v1 = np.array([9, 10, 7, 7, 9])
v2 = np.array([2, 0, 5, 1, 4])
v3 = np.array([4, 0, 0, 4, 1])
v4 = np.array([3, -4, 3, -1, -4])
A = np.array([v1, v2,v3,v4])
print(A)
print(np.linalg.matrix_rank(A))
print('Матрица Грама:\n',A@A.T)
print(np.linalg.det(A@A.T))
print(np.linalg.inv(A@A.T))
