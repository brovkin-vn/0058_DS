import numpy as np
import cvxpy
c = np.array([[2, 5, 3], [7, 7, 6]])
x = cvxpy.Variable(shape=(2, 3), integer=True)
constraint = [cvxpy.sum(x[0]) <= 180, 
              cvxpy.sum(x[1]) <= 220, 
              cvxpy.sum(x[:, 0]) == 110, 
              cvxpy.sum(x[:, 1]) == 150, 
              cvxpy.sum(x[:, 2]) == 140, 
              x >= 0]
total_value = cvxpy.sum(cvxpy.multiply(c, x))
problem = cvxpy.Problem(cvxpy.Minimize(total_value), constraints=constraint)
r = problem.solve(solver='ECOS_BB')
print(r)