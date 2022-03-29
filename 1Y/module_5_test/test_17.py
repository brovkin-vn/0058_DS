import numpy as np

def grad(x,y,z):
    dx = 4*x - 4*z + 4
    dy = 8*y - 8*z + 8
    dz = -4*x - 8*y + 18*z - 20
    return(dx,dy,dz)

alfa = 1
gamma = 0.25
x_cur = (1, 2, -5)
x_prev = (0,0,0)
# x_new = x_cur - x_prev
print(grad(*x_cur))