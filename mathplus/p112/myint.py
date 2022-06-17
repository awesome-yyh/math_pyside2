## 1 diff to int
from sympy import *
x = symbols('x')
df = 15*x**2-2*x;
# df = 4*x+2/x**2;
# df = (x+1)/sqrt(x);
# df = 1/(1+x**2)-1/x;
##
f = integrate(df,x)
print(simplify(f))
