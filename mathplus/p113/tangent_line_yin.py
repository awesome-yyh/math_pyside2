from sympy import *
t = symbols('t')
# x =t-sin(t);y=8-cos(t);t0 = pi/3;
x = t**4+3;y=t**3+t;t0=1;
##
dydx = diff(y) / diff(x);
k = dydx.subs(t,t0);
x0 = x.subs(t,t0);
y0 = y.subs(t,t0);

b = -k*x0+y0;
print('tangent line: y = %f*x+%f' % (k,b))
print(simplify(k))
print(simplify(b))