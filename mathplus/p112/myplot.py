from sympy import *
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x')
##
y = 1/(1+exp(-x));
# y = sin(x)
xx = [-pi*2, pi*2]
##
nx = np.linspace(float(xx[0]), float(xx[1]), 1000)
ly = lambdify(x,y)
ny = ly(nx)
plt.plot(nx,ny)
plt.show()
