## 11 approximate 
from sympy import *
x = symbols('x')
# y = sqrt(1-x); a = 0;
# y=sqrt(x); a=1;
# y=2*exp(x-x**2); a=1;
# y = exp(3*x)+3*x+1; a = 0;
# y = 4+exp(3*x); a = 0;
# y = 1*exp(x)-6; a =0;
# y = exp(x); a = 0;
# y = sin(x)+cos(x);a=0;
# y = cos(x)-sin(x); a = 0;
# y = sin(sin(x)); a=pi;
# y = sin(2*x); a = pi/2;
# y = x**3+4/x**2; a = 2;
# y = x**3-9*x-5; a = 7;
# y = x**4-8*x+11; a = 1;
# y = x**(4); a=2;
# y = 1/x; a = 4;
# y=exp(x**2-x);a=2;
y = 
aa = 1.99;  # b question
##
k = diff(y).subs(x,a); b = -k*a+y.subs(x,a); 
print('tan line: y = %f*x+%f\n' %(k,b))
print('k: ', k)
print('b: ', b)
approximate = (k*x+b).subs(x, aa); 
print('guji: %f\n' % approximate)
ddy = diff(diff(y))
ddy0 = ddy.subs(x, aa); 
print('second diff value: %f\n' % ddy0,ddy0)
if ddy0 > 0:
    print('up(ao)--> smaller')
else:
    print('down(tu)-->larger')
