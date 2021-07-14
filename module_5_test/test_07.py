from scipy.stats import norm 
alpha = 0.01
alpha = -norm.ppf(alpha/2)
print(alpha) # 2.17
_x = 7.6
std = 0.8
n = 60
dmu = alpha* std / n**0.5
print(round(_x - dmu, 2), round(_x + dmu, 2))
