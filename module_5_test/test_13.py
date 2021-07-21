import numpy as np
import cvxpy
c = np.array([[1000, 12, 10, 19, 8]
    ,[12, 1000, 3, 7, 2]
    ,[10, 3, 1000, 6, 20]
    ,[19, 7, 6, 1000, 4]
    ,[8, 2, 20, 4, 1000]
    
])
x = cvxpy.Variable(shape=(5, 5), boolean=True)
constraint = [cvxpy.sum(x, axis=0) == np.ones(5),
              cvxpy.sum(x, axis=1) == np.ones(5)]

func = cvxpy.sum(cvxpy.multiply(x, c))

problem = cvxpy.Problem(cvxpy.Minimize(func), constraints=constraint)
r = problem.solve(solver='ECOS_BB')
print(r)