from sympy import *
x = symbols('x')
##
y = 75-x;
##
a = x*y**2;
x0 = solve(diff(a));
x0 = min(x0);
y0 = y.subs(x,x0)
area = a.subs(x,x0)
print('a: ',x0,'b: ',y0, 'area:', area)