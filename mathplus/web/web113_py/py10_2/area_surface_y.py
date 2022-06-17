from sympy import *
t = symbols('t')
# x = exp(t)-t; y = 4*exp(t/2); xx = [0 4];
# -2*Pi*Integrate[(x - Exp[x])*(Exp[x] + 1), {x, 0, 3}]
x = 3*t**2; y = 2*t**3;xx = [0,4];
# x0 = 0; x1 = 4;
# xx = solve(x-y);x0 = xx[0]; x1 = xx[1];
##
x0 = xx[0];x1 = xx[1];
u = diff(x)**2+diff(y)**2;
s = integrate(2*pi*x*sqrt(u),(t,x0,x1));
print(simplify(abs(s)))