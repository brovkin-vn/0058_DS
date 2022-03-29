import numpy as np
m = np.array([20,23,29,22,50,43,35,98,28])
r = np.array([70,65,58,90,45,57,50,90,38])
print(np.sort(m))
print(np.sort(r))
print(round(2/7,2))
print(round(np.mean(m),2))
print(round(np.mean(r),2))
print(round(np.std(m),2))
print(round(np.std(r),2))
print(round(np.std(m, ddof=1),2))
print(round(np.std(r, ddof=1),2))
print(round(np.corrcoef(m,r)[0,1],2))

