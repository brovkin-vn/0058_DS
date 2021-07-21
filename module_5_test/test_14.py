import numpy as np
import cvxpy as cvx

x = cvx.Variable(shape=(5,5), boolean=True)
u = cvx.Variable(shape=5, integer=True)
from itertools import product
constraints = [
    cvx.sum(x, axis=0) == np.ones(5),
    cvx.sum(x, axis=1) == np.ones(5),
    u >= 0,
    u <= 4,
    cvx.sum(cvx.diag(x)) == 0
]
for i, j in product(range(5), range(5)):
    if i >= 0 and j >= 1 and i != j:
        constraints.append(u[i] - u[j] + 5 * x[i,j] <= 4)
d = np.array([[0, 12, 10, 19, 8], 
              [12, 0, 3, 7, 2], 
              [10, 3, 0, 6, 20], 
              [19, 7, 6, 0, 4], 
              [8, 2, 20, 4, 0]])
func = cvx.sum(cvx.multiply(x, d))
problem = cvx.Problem(cvx.Minimize(func), constraints=constraints)
result = problem.solve(solver='ECOS_BB')
print(np.round(result))