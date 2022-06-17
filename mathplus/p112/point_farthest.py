from sympy import *
x = symbols('x')
##
y2 = 4-4*x**2; #y^2
xy0 = [1, 0];
##
z2 = (x-xy0[0])**2+(sqrt(y2)-xy0[1])**2;
x1 = solve(diff(z2))
y1 = sqrt(y2.subs(x,x1[0]))
print('x1: ', x1)
print('y1: ', y1)
