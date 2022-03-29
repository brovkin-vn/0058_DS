from scipy.stats import t
from scipy.stats import norm
import math


v1 = 132
n = 189
_p = v1 / n
print(round(_p, 3))
alpha = 0.1
z = -norm.ppf(alpha / 2)
print(z)
z2 = -t.ppf(alpha / 2, n - 1)
print(z2)
dp = z * math.sqrt(_p * (1-_p) / n)
print(round(_p - dp, 3), round(_p + dp, 3))