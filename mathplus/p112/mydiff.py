from sympy import *
x = symbols('x')       
# f = 20*x**(2/3);
# f = sqrt((120-20*x)**2+(80-10*x)**2);
# f = 96+80*x-16*x**2;f=diff(f);
# f=x/(3*x+2);
# f=2*atan(3*x);
# f=6*x**(5/3)-12*x**(1/3);
# f=sin(x)*(tan(x)-cos(x));
f = tan(x)
##
print(simplify(diff(f)))