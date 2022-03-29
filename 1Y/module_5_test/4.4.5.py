import numpy as np
import math

a = np.array([1.23,2.35,2.75])
y = np.array([1.01,12.3,2.74])
m = len(a)
mse = 1/m * np.nansum((a-y) ** 2)
print(mse)
rmse = math.sqrt(mse)
print(round(rmse, 2))