from sympy import *
import numpy as np
x = symbols('x')
y = x**3; xx = [-3, 3]; n = 6;
# y=60/x+x-1; xx=[2, 6]; n = 4;
##
x0 = xx[0]; x1 = xx[1];
delta = (x1-x0)/n;
# Left Rule
nx = np.linspace(float(x0), float(x1)-delta, n)
ly = lambdify(x,y)
nxl = ly(nx)
ln = delta * sum(nxl)
print(nxl)
print('l = %f \n'% ln)