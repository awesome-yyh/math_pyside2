# Semicircle
from sympy import *
yi = symbols('yi')
r = 2;
d = 2;
##
xi = sqrt(r**2-(yi-d)**2);
F = 2*integrate(xi*yi, (yi, d, d+r)) # right*2
print("%g" % F.evalf(), '最后结果*delta')
print(simplify(F))