import numpy as np  
A=np.matrix("1,2;2,5")
# print(A)
# print(np.linalg.inv(A))
# print(np.linalg.det(A))
A=np.matrix("1,2;1,1")
B=np.matrix("5,-2;-1,4")
# print(np.linalg.det(A))
# print(np.linalg.det(B))
# print(np.linalg.det(A+B))
A=np.matrix("2,0,0;0,1,0;0,0,4")
# print(np.linalg.det(A))
# print(np.linalg.det(np.linalg.inv(A)))

A=np.matrix("1,0,3,5;0,4,5,5")

print(np.linalg.matrix_rank(A))

