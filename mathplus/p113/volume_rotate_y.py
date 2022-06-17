from sympy import *
x = symbols('x')
##
y1 = 9*x-x**2;y2=0;xx = solve(y1-y2);d = 11;
# y1 = 8*x; y2 = 2*x**3;xx = solve(y1-y2);d = 2;xx = [0, 2];
# y1 = x; y2 = 0*x**2;xx = solve(y1-y2);d = 1;xx = [2, 4];
# y1 = 2*(x-2)**2; y2 = 8; xx = solve(y1-y2); d = -1;
# y1 = 5*x; y2 = 5*x**4; xx = solve(y1-y2); d = 1;
# y1 = sin(x); y2 = cos(x); xx = solve(y1-y2);d = pi/2; xx = [0, pi/4];
# y1=sqrt(25-(x-0)**2);y2=5;xx=[0, 5];d=5;
##
x0 = xx[0]; x1 = xx[1];
c = 2*pi*(x-d);
h = y1-y2;
v = integrate(c * h, (x,x0, x1));
v = abs(v)
print("%g" % v.evalf())
print(simplify(v))
