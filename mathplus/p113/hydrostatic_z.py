# oblique square
from sympy import *
x = symbols('x')
##
a = 7;
ro = 100;
## 
h = a; w = a; d = (a*sqrt(2)/2-a/2);
# delta = ro*9.8;
delta = ro;
##
F = integrate(delta * x * w, (x,d, d+h));
print("%g" % F.evalf())
print(simplify(F))
