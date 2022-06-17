from sympy import *
x = symbols('x')
##
# y = sqrt(2*x+3);xy=[4, 0];
# y = (5-3*x)/4;xy = [1, -3];
# y = 3-2*x; xy = [-3, 1];
y = 8/x; xy = [3, 0];
##
x0 = xy[0];y0 = xy[1];
L2 = (x-x0)**2+(y-y0)**2;
x1 = solve(diff(L2))
y1 = y.subs(x,x1[0])
L = sqrt(L2.subs(x,x1[0]))
print('x1: ',x1, '\ny1: ', y1, '\nL: ', L)
