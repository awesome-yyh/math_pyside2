from sympy import *
t = symbols('t')
##
x = 9/2*t**2; y = 9*exp(1*t); t0=-2;
# x = t**2; y = t**3-2*t; t0 = -1;
# x = t**2-t; y = 2*sqrt(t); t0 = 1;
##
dydx = diff(y) / diff(x);
dydx0 = dydx.subs(t, t0)
print('dydx: ', dydx)
d2 = diff(dydx)/diff(x);
d20 = d2.subs(t, t0)
print('d2: ', d2)
print('d20: ', d20)