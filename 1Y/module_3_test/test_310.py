import numpy as np

s=np.array([33,65,50,45])
print(len(s))
print("ndi,", s.ndim)
print("shape", s.shape)

apartment = np.array([59.50, 31.40, 19, 22, 60550, 2])
share_living_space = apartment[1]/apartment[0]
apartment = np.delete(apartment, [0, 1])
apartment = np.append(apartment, share_living_space)
print(apartment)
print(apartment.shape)
t = np.array([12, 14, 17, 19, 24, 28, 31, 31, 27, 22, 17, 13])
print(np.mean(t))
a = np.array([120,150,90])
b = np.array([130,130,130])
c = np.array([2,3,2.5])
print(c*1000*72)
a = a
b = b
c = c*72
d = a+b+c
print(d)
x = np.array([4,5])
y = np.array([2,1])
u = np.array([1,0])
z=2*x -3*y + 5*u
print(z)
a = np.array([3,4,5,9])
b = np.array([1,5,3,6])
d = 400*b - 200*a
print(d)

a = np.array([4,5,-1])
b = np.array([2,0,1])
print(np.dot(a, b))

import math
x = np.array([4,6,1])
print(math.sqrt(np.dot(x,x)))

