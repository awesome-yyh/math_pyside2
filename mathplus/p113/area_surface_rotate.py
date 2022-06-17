from sympy import *
x = symbols('x')
##
y = sqrt(9-x**2);xx=[-1,1];flag='x';
# y = 5*exp(x-3);xx=[4,9];flag='x';
# y = 5-x**2;xx=[0,3];flag = 'y';
# y = 1*x**(3); xx = [3, 4]; flag = 'x';#x<-->y
# y = x**3; xx = [0, 2];flag ='x';
# y = (24*x+8)/7;xx=[0, 7];flag = 'x';
# y = x**3/6 + 1/(2*x); xx = [1, 3]; flag = 'x';
# y = 2/9*x**(3/2); xx = [0, 7]; flag = 'y';
# y = x**3; xx = [0, 3]; flag = 'x';
# y = x**2/4 - log(1*x)/2;xx = [3, 5]; flag = 'y';
# y = 3/4*x**2 - x**4/16;xx = [0, 2*sqrt(3)];flag = 'x';
# y=1+2*x**2;xx=[1, 2];flag='y';
##
x0 = xx[0]; x1 = xx[1];
dy = diff(y);
if flag == 'y':
    u = 2*pi*x*sqrt(1+dy**2); #about x--y, about y--x
elif flag == 'x':
    u = 2*pi*y*sqrt(1+dy**2); #about x--y, about y--x
##
print('integral factor: ')
print(simplify(u))
s = integrate(u,x, (x, x0, x1));
print(float(s))
# s = abs(s)
# print('result: ')
# print("%g" % s.evalf())
# print(simplify(s))
