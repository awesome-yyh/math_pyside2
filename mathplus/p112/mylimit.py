from sympy import *
x = symbols('x')
##
y = (x**2+1)/(5*x);
# y = 4*x/(x**2-9);
# y = (x-1)/x**2;
# y = 1/(x**2-16);
x0 = oo;
##
lim = limit(y,x,x0);
print(lim)
