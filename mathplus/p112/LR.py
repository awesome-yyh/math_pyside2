from sympy import *
import numpy as np
x = symbols('x')
## 
# y = 3*x*exp(x); x0 = 0; x1 = 1; n = 5*2*2;
# y = 9/x**2; x0 = 1; x1 = 2; n = 5*2*2;
# y = (x+4)*(x-8)**2; x0 = -3; x1 = 9; n = 4;
# y = 15/x + x-0; x0 = 1; x1 = 7; n = 3;
# y = 1*x**2+0; x0 = 0; x1 = 2; n = 4;
# y = 1/x; x0=1;x1 = 4; n =4;
# y = (cos(x))**2; x0 = pi/6; x1 = pi/2; n = 4;
# y = 3+4*x**2;x0=-1;x1=2;n=3;
y = 5*x**2-4*x;x0=0;x1=3;n=6
## comm
delta = (x1-x0)/n;
inte = integrate(y, (x,x0, x1));
print(inte)
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
