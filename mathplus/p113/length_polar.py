from sympy import *
import numpy as np
st = symbols('st')
##
# r = 4*sin(st); xx = [0, 1/3*pi];
r = 5+5*sin(st);xx = [0, pi*2];
# r = (cos(st/4))**4;xx = [0, 4*pi]; #区间第二项 st/几就是几乘π
# r = st**2; xx = [0, 2*pi];
# r = st; xx = [0, pi*2];
# r = 2-2*cos(st);xx = [0, pi*2];
# r = 1-sin(st);xx = [0, pi*2];
# r = 5*(sin(st/2))**2; xx=[0, pi/2];
# r=4*cos(st/ 2)**2; xx=[0, pi/2];
##
st0 = xx[0]; st1 = xx[1];
u = (r**2 + (diff(r))**2)**(1/2);
# u = st**2
##
print('integral factor: ')
print(simplify(u))

print('num int')
nx = np.linspace(float(st0), float(st1), 10000)
lu = lambdify(st,u)
nu = lu(nx)
s = np.trapz(nu, nx)
print('result: ')
print("%g" % float(s))
print(simplify(s))

print('sym int')
s = integrate(u, (st,st0, st1));
s = abs(s)
print('result: ')
print("%g" % float(s))
print(simplify(s))
