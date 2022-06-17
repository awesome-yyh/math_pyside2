from sympy import *
h = symbols('h')
th = 12; 
tr =  3;
thh = 2.5;
tdelta = 210;
##
a=tdelta*pi*(tr/th*(th+thh-h))**2*h;
s = integrate(a,(h, thh,thh+th))
print("%g" % s.evalf())
print(simplify(s))
