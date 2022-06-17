from sympy import *
y = symbols('y')
##
s = 18; #up
x = 8; #down
z = 15; #
ro = 62; #
##
xi = (s-x)*(z-y)/z;
delta = (x+xi)*y;
s = integrate(delta*ro,(y,0,z))
print("%g" % s.evalf())
print(simplify(s))
