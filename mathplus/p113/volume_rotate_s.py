from sympy import *
x = symbols('x')
b = 2;
h = 4;
d = 6;
##
y1 = (b/2-x)/(b/2)*h+d; y2 = d;
x0 = 0; x1 = b/2;
a = 2*pi * (y1**2 - y2**2);#right*2
v = integrate(a, (x,x0, x1));
v = abs(v)
print("%g" % v.evalf())
print(simplify(v))