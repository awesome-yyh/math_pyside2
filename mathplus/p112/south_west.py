from sympy import *
am = 10;
ds = 15;
dw = 20;
##
t = 12-am;
s = ds*t;
w = dw*t;
z = sqrt(s**2+w**2);
dz = (s*ds+w*dw)/z
print(dz)
