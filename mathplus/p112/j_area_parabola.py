from sympy import *
x = symbols('x')
##
y = 11-x**2;
##
a = (2*x)*y;
x0 = max(solve(diff(a)));
width = 2*x0;
print('width = ', simplify(width))
height = y.subs(x,x0);
print('height = ', simplify(height))
area = a.subs(x,x0);
print('area = ', simplify(area))
