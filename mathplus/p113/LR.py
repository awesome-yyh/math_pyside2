from sympy import *
import numpy as np
x = symbols('x')
## 
# y = 3*x*exp(x); x0 = 0; x1 = 1; n = 5*2*2;
# y = 9/x**2; x0 = 1; x1 = 2; n = 5*2*2;
# y = (x+2)*(x-16)**2; x0 = -1; x1 = 17; n = 6;
# y = 60/x + x-1; x0 = 2; x1 = 6; n = 4;
# y = x**2; x0 = 0; x1 = 2; n = 4;
# y = 1/x; x0=1;x1 = 4; n =4;
y = 4+2*x**2;x0=-1;x1=2;n=6
## comm
delta = (x1-x0)/n;
inte = integrate(y, (x,x0, x1));
ly = lambdify(x,y)
## L Rule
xl = np.linspace(x0, x1-delta, n)
ln = delta * sum(list(ly(xl)));
le = inte - ln;
print('l = %f  le = %f' % (ln, le))
## R Rule
xr = np.linspace(x0+delta, x1, n)
rn = delta * sum(ly(xr));
re = inte - rn;
print('r = %f  re = %f' % (rn, re))
#
print("delat: ", delta)
print('left: ', ly(xl))
print('right: ', ly(xr))
