from sympy import *
t = symbols('t')
##
# x = 6*cos(t)+cos(6*t);  y = 6*sin(t)-sin(6*t);tt = [0, pi];
# x = t**2 - 5*t; y = sqrt(t); tt = solve(y); #t1 = 1/2*(3+sqrt(5));
# x = 3 + exp(t); y = t - t**2;tt = solve(y);
x = 2*sqrt(t); y = 3*t-t**2;tt = [0, 1]; 
t0 = min(tt);t1 = max(tt); 
##
u = y*diff(x);
##
print('integral factor: ')
print(simplify(u))
s = integrate(u,(t, t0, t1));
s = abs(s)
print('result: ')
print("%g" % s.evalf())
print(simplify(s))
