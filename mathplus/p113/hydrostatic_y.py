# circle
from sympy import *
r = 6; 
d = 120; 
# s = r**3*d*pi #feet时不乘9.8
s = r**3*d*pi*9.8 #否则要乘9.8
print(simplify(s))
print('%g' % s)