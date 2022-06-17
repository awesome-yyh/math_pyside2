from sympy import *
x = symbols('x')
##
y = 3*x**2; xx = [-1, 1];fy = sqrt(x/3); #y-fan hanshu
##
h = y.subs(x,xx[0]);
da = 2*x*fy;
s = integrate(da,(x,0,h))
print(s,'*delta')
