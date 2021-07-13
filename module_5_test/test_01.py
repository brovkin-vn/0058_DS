# x1 = 1
# x2 = 1
# L = (2.1 - x1 - x2)**2 + (2.9 - x1 - 3*x2)**2 +  (4.1 - x1 - 5*x2)**2
# print(L)
c0 = 0.02
c1 = 0.2
c2 = 0.78
c0c = 0.70
c1c = 0.10
c2c = 0.04
print(c0*c0c)
print(c1*c2c)
print(c2*c2c)
print(c0*c0c + c1*c1c + c2*c2c)
print(c2*c2c/(c0*c0c + c1*c1c + c2*c2c))