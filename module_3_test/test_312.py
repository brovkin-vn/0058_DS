import numpy as np

Husband_Income = np.array([100,220,140])
Wife_Income = np.array([150,200,130])
Mother_In_Law_Income = np.array([90,80,100])

Husband_Consumption = np.array([50,50,60])
Wife_Consumption = np.array([100,80,140])
Mother_In_Law_Consumption = np.array([100,20,140])

A = np.array([Husband_Income, Wife_Income, Mother_In_Law_Income]).T
B = np.array([Husband_Consumption, Wife_Consumption, Mother_In_Law_Consumption]).T
print(A)
print(B)
print((A*0.87)[0])
print(str(list((A*0.87)[0])).replace(' ' ,''))
P=A*0.87 - B
print(str(list(P[2])).replace(' ' ,''))
print(str(list((A*0.87)[0])).replace(' ' ,''))

