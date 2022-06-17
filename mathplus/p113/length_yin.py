from sympy import *
t = symbols('t')
##
# x = t/(2+t); y = log(2+t); tt = [0, 3];
x = exp(5*t)-5*t; y = 4*exp(5/2*t); tt = [0, 5];
# x = t*cos(t); y = t*sin(t); tt = [0, 1];
## distance
t0 = tt[0]; t1 = tt[1];
dx = diff(x); dy = diff(y);
u = (dx**2 + dy**2)**(1/2);
##
print('integral factor: ')
print(simplify(u))
## 
s = integrate(u,(t, t0, t1));
s = abs(s)
print('result: ')
print("%g" % s.evalf())
print(simplify(s))
