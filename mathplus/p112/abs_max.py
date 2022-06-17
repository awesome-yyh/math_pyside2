from sympy import *
import numpy as np
x = symbols('x')
##
# y = 1*x**3+3*x**2-9*x+4; xx = [-2, 2];
# y=x*sqrt(4-x**2);xx=[-1, 2];
y = 7*tan(4*x);xx=[pi/16,pi/12]
##
x1 = solve(diff(y));
xx1 = [x for x in x1 if (x >= xx[0] and x <= xx[1])]
xxx =list(set(xx1+xx));
print(xxx)
v = []
for x0 in xxx:
    v.append(y.subs(x,x0))
print(v)
vmax = max(v);vmin = min(v);
print('max: ', vmax, 'min: ', vmin)
print('max: ', float(vmax), 'min: ', float(vmin))
print(y.subs(x,0))
print(y.subs(x,pi))