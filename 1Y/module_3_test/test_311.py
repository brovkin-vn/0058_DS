import numpy as np
import pandas as pd

Hut_Paradise_DF = pd.DataFrame({'1.Rent': [65, 70, 120, 35, 40, 50, 100, 90, 85], 
                                '2.Area': [50, 52, 80, 33, 33, 44, 80, 65, 65], 
                                '3.Rooms':[3, 2, 1, 1, 1, 2, 4, 3, 2],
                                '4.Floor':[5, 12, 10, 3, 6, 13, 8, 21, 5], 
                                '5.Demo two weeks':[8, 4, 5, 10, 20, 12, 5, 1, 10], 
                                '6.Liv.Area': [37, 40, 65, 20, 16, 35, 60, 50, 40]})

A = Hut_Paradise_DF.values
print(A[4,:])
print(str(list(A[:,3])).replace(' ' ,''))
print(A[2,3])
print(A[:,0].shape)
# Вычислите вектор нежилой площади:
print(A[:,1])
print(A[:,5])
print(str(list(A[:,1]-A[:,5])).replace(' ' ,''))
# Арендная плата
print(str(list(A[:,0]*4/10)).replace(' ' ,''))
a=pd.DataFrame({'time':[10,20,30,15,5,40,20,8,20]}).values[:,0]
print(a)
print(A[:,5])
print(str(list(A[:,4]*a)).replace(' ' ,''))
print(A[:,4]@a)

u=np.array([3,0,1,1,1])
v=np.array([0,1,0,2,-2])
w=np.array([1,-4,-1,0,-2])
print(str(list( 2*v + -3*w )).replace(' ' ,''))
print(round((u/np.linalg.norm(u))[2],3))
print(round((v/np.linalg.norm(v))[3],3))
print(round((w/np.linalg.norm(w))[0],3))
