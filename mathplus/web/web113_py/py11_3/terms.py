from sympy import *
import numpy as np

n = symbols('n')
# y= (-1)**n/(10**n*factorial(n));e = 10**(-5); tn = 5;
# y = 1/(n*log(n)**3); e = 0.1;tn =3;
# y = (n+3)/n**6; e = 0.001; tn = 4;
# y = 1/n**2; tn = 7; e = 0.00005; #这个+1
# y = (-1)**(n+1)/n**n; e = 0.05; tn = 5;
y = 1/(n**2+1);e = 0.001; tn = 6;
# y = 1/(3**(n-1)+1); e = 10**(-2); tn = 5;
##
sn = 0
for i in range(1,tn+1):
    sn += y.subs(n,i)
print('(a): %.7f\n' % sn)

sn = integrate(y,(n,tn,oo));
print('(b): %.7f\n' % float(sn))

n = 1/e
print(n)