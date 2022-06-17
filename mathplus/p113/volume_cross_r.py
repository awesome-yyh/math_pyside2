from sympy import *
x = symbols('x')
r = 4;
##
y = sqrt(r**2-x**2);
delta = 1/2*(2*y)**2;
v = integrate(delta,(x,-r,r))
v = abs(v)
print("%g" % v.evalf())
print(simplify(v))
