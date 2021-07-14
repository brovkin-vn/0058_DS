from scipy.stats import t
from scipy.stats import norm
import math
# 0.95 - доверительный интервал, 100-1 число степеней свободы
# для двустороннего t-теста
value = t.ppf((1 + 0.95)/2, 100-1)
print(value) # 1.98

def confidence_interval_norm(alpha, sigma, n, mean):
    value = -norm.ppf(alpha / 2) * sigma / math.sqrt(n)
    return round(mean - value), round(mean + value)

def confidence_interval_t(alpha, s, n, mean):
    value = -t.ppf(alpha / 2, n - 1) * s / math.sqrt(n)
    return round(mean - value), round(mean + value)

alpha = 0.01
s = 400
n = 15 
mean = 2000    

v = confidence_interval_t(alpha, s, n, mean)    
print(v)

alpha = 0.01
sigma = 1150
n = 250
mean = 3540
v = confidence_interval_norm(alpha, sigma, n, mean)
print(v)

