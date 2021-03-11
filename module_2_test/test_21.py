import numpy as np

my_secret = [x for x in range(1, 301, 7) if x%10 == 7 or x%10 == 1]

arr = np.array([my_secret, [x/2 for x in my_secret], [x-100 for x in my_secret]])

print(arr)