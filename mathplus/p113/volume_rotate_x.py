from sympy import *
x = symbols('x')
## 
# y1 = 2/5*x**2; y2 = 7/5-x**2; xx = solve(y1-y2); d = 0;
# y1 = 9-25*x**2; y2 = 0; xx = solve(y1-y2); d = 0;
# y1 = 7*x**4; y2 = 7*x; xx = solve(y1-y2); d = 0; #xx = [0, 1]; 
# y1 = 3*x**2; y2 = 3; xx = solve(y1-y2);d = 3;# xx = [0, 1];
# y1 = 5*x**2; y2 = 5*x; xx = solve(y1-y2); d = 0;#xx=[0, 1];
# y1 = 6-3/2*x; y2 = 0; xx = [0, 1];  d = 0;
# y1 = 4/x; y2 = 0; xx = [1, 3]; d = -1;
# y1 = 5*x; y2 = 5*sqrt(x); xx = solve(y1-y2); d = 5;
# y1 = sqrt(2*x+4); y2 = 0; xx = [0, 5]; d = 0;
# y1 = cos(x/2); y2 = sin(x/2); xx = [0, pi/2]; d = pi;
# y1 = -1*cos(x); y2 = -1*sin(x); xx = [0, pi/4]; d = 0;
y1 = -2*x**2+4*x+1; y2 = 1; xx = solve(y1-y2); d = 1;
# y1 = x; y2 =sqrt(x);xx = solve(y1-y2); d = 0;
# y1 = -10/3*x +11; y2 = 6; xx = [0, 3/2]; d = 0;
# y1 = 2*(x-2)**2; y2 = 8; xx = solve(y1-y2); d = -1;
# y1 = sqrt(2*x); y2 = 0; xx = [0, 3]; d = 0;
# y1 = (x-1)**2; y2 = 3*x-3; xx = solve(y1-y2); d = 0;
# y1 = sqrt(1-x**2); y2 = 1; xx=[0, 1];d = 1;
##
x0 = xx[0]; x1 = xx[1];
a = pi * ((y1-d)**2 - (y2-d)**2);
v = integrate(a, (x,x0, x1));
v = abs(v)
print("%g" % v.evalf())
print(simplify(v))
