## 1 diff to int
from sympy import *
x = symbols('x')
df = cos(x)**2;xx=[0, pi/6];
##
f = integrate(df,(x,xx[0],xx[1]))
print(simplify(f))
print(f)
