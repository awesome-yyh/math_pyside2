from sympy import *
x = symbols('x')
# y = x*log(1+x**2);a = 0; n = 7;
y = exp(x); a = 0; n = 5;

print(y.series(x, a, n))
