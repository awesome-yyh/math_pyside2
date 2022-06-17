from sympy import *
x = symbols('x')
##
v = 1/3 * pi*(3*x)**2 * x;
dvdt = 18;
h0 = 9;
##
dvdx = diff(v);
dxdt = 1/dvdx * dvdt; 
print(dxdt.subs(x,h0))
print(dvdx.subs(x,h0)*dvdt)
