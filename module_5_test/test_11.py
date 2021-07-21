import numpy as np
import cvxpy
from scipy.optimize import linprog

values = [4, 2, 1, 7, 3, 6]
weights = [5, 9, 8, 2, 6, 5]
C = 15
n = 6

c = - np.array(values)
A = np.array(weights)         #shape = (6,)
A = np.expand_dims(A, 0)      #shape = (1,6)
b = np.array([C])


print(linprog(c=c, A_ub=A, b_ub=b))

x = cvxpy.Variable(shape=n, integer = True)
constraint = (A @ x <= b)
total_value = c * x

problem = cvxpy.Problem(cvxpy.Minimize(total_value), constraints=[constraint])

print(problem.solve())

print(x.value)