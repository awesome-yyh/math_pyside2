from sympy import *
x = symbols('x')
##
# y = (x**2+1)/(5*x);
# y = 4*x/(x**2-9);
# y = (x-1)/x**2;
y = 1/(x**2-16);
a = [1, 2]; #undefined x
##
hz = limit(y,x,oo);
hf = limit(y,x,-oo);
print('水平渐近线：y=%f, y=%f\n' % (hz,hf))
a0l = limit(y,x,a[0],'-')
a0r = limit(y,x,a[0],'+')
a1l = limit(y,x,a[1],'-')
a1r = limit(y,x,a[1],'+')
print("a0 point: ", a0l, a0r)
print("a1 point: ", a1l, a1r)
