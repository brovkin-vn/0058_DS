import numpy as np
from sklearn.metrics import accuracy_score
a = np.arange(100)
b = np.arange(100)
a.fill(100)
b.fill(100)
a[0] = 555
acc = accuracy_score(a, b)
print(a)
print(round(acc, 2))
