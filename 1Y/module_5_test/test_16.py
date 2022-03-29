from scipy import optimize

def f(x, y):
    return (2.1-x-y)**2 + (2.9-x-3*y)**2 + (4.1-x-5*y)**2



r = optimize.minimize(lambda x: f(*x), x0=(10, 10))
print(r)
print(f(1.53333,0.5))