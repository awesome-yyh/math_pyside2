from sympy import *
x = symbols('x')
## 
l =       2;
h =       3;
delta = 130;
## 
w = l/h*x;
F = integrate(delta* (h - x) * w, (x,0, h));
print("%g" % F.evalf())