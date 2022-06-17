# open top, ding is kong, di is square
from sympy import *
x = symbols('x')
##
v = 4; # volume
##
h = v / x**2;
a = x**2 + 4*x*h;
print(a)
x0 = solve(diff(a))[0]
height = h.subs(x,x0);
area = a.subs(x,x0);

print('height = ', simplify(height))
print('length of base = ', simplify(x0))
print('area = ', simplify(area))
print('unit is "meters" if 4 cubic meters')
