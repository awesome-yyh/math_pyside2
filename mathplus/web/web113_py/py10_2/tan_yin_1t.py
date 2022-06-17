from sympy import *
t = symbols('t')
cc = 13; t0 = 4/3*pi; x = cc*(t-sin(t)); y = cc*(1-cos(t)); 
# x = exp(sqrt(t)); y = t-log(t**4); t0 = 1;
# x = t - t**(-1); y = 5 + t**2; t0 = -1;
# x = t**4+2      ; y = t**3 + t; t0 = 1;
# x = 3*cos(t); y = 5*sin(t)*cos(t);
# x = cos(t)+sin(2*t); y = sin(t)+cos(2*t); t0 = 0;
##
dy = diff(y); dx = diff(x);
dydx = dy/dx;
x0 = x.subs(t,t0); y0 = y.subs(t,t0);
dydx0 = dydx.subs(t, t0);
print('y = %g*x+%g\n' % (dydx0,-dydx0*x0+y0))
print('k=')
print(simplify(dydx0))
print('b=')
print(simplify(-dydx0*x0+y0))