from scipy.stats import norm
from scipy.stats import t
from math import sqrt
import pandas as pd
import math

# alpha = 0.95
# n = 100
# k = n - 1
# value = t.ppf((1 + alpha)/2, k)
# print(round(value, 2))

# alpha = 0.99
# n = 10
# k = n - 1
# value = t.ppf((1 + alpha)/2, k)
# print(round(value, 2))

# mean = 14
# n = 64
# X_ = 13.5
# alpha = 0.05
# sigma = 2
# Zst = (X_-mean) / (sigma/sqrt(n)) # когда sigma изветстна
# # Zst = (X_-mean) / (s/sqrt(n)) # когда sigma неизветстна
# print(Zst)
# p_value = norm.cdf(Zst)
# print(round(p_value, 3))

# mean = 455
# n = 16
# X_ = 449
# alpha = 0.05
# sigma = 12.5
# s = 455
# Zst = (X_-mean) / (sigma/sqrt(n)) # когда sigma изветстна
# # Zst = (X_-mean) / (s/sqrt(n)) # когда sigma изветстна
# print(Zst)
# p_value = norm.cdf(Zst, 0, 1)
# print(round(p_value, 3))

# mean = 6.5
# n = 25
# X_ = 7.0
# alpha = 0.05
# sigma = 1.4
# Zst = (X_-mean) / (sigma/sqrt(n)) # когда sigma изветстна
# # Zst = (X_-mean) / (s/sqrt(n)) # когда sigma изветстна
# print(Zst)
# p_value = norm.cdf(Zst)
# print(round(1-p_value, 3))mean = 6.5

# mean = 12000
# n = 135
# X_ = 11500
# alpha = 0.05
# sigma = 5110
# Zst = (X_-mean) / (sigma/sqrt(n)) # когда sigma изветстна
# # Zst = (X_-mean) / (s/sqrt(n)) # когда sigma изветстна
# print(round(Zst, 3))
# p_value = norm.cdf(Zst)
# print(round(p_value, 3))

# df = pd.DataFrame({
#     'X': [6.1, 9.2, 11.5, 8.6, 12.1, 3.9, 8.4, 10.1, 9.4, 8.9]
# })
# std = df.X.std()
# n = df.X.count()
# k = n - 1
# mean = df.X.mean()
# X_ = 10
# alpha = 0.05
# Zst = (X_-mean) / (std/sqrt(n)) # когда sigma изветстна
# print(round(Zst, 3))
# p_value = 1-t.cdf(abs(Zst), k)
# print(round(p_value, 3))

# доверительный интервал
# n = 185
# k = n - 1
# n_ = 77
# p = 0.35
# p_ = n_/n
# print(p, p_)
# Zst = (p_ - p) / sqrt(p * (1-p)/n)
# # Zst = (0.42-0.35) / sqrt(0.35*(1-0.35)/185)
# Zst = round(Zst, 3)
# # Zst = 1.89
# print(Zst)
# p_value = (1-t.cdf(abs(Zst), k))
# print(round(p_value, 3))

n = 125
k = n - 1
n_ = 87
p = 0.75
p_ = n_/n
print(p, p_)
Zst = (p_ - p) / sqrt(p * (1-p)/n)
# Zst = round(Zst, 3)
print(Zst)
p_value = 1-t.cdf(abs(Zst), k)
print(round(p_value, 3))
