from sympy import *
x = symbols('x')
x2 =  1;
y2 =  1;
ac =  36;
##
b = ac/y2; y2x2 = x2/y2;
A = b - y2x2*x**2;
a2 = ac/x2; a = sqrt(a2);
v = 2 * integrate(A,(x,0,a))
v = abs(v)
print("%g" % v.evalf())
print(simplify(v))
