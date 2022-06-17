#1Mean Value ; 2Newton
from sympy import *
x = symbols('x')
# f = 1*x**3+1*x-9; xx = [0, 2]; v=solve( (f.subs(x,xx[1]) - f.subs(x,xx[0])) / (xx[1] - xx[0]) - diff(f) ) ;print(v)#Mean Value
y = x**3+x+8; x1 = -2;    x2 = x1 - y.subs(x,x1)/diff(y).subs(x,x1);print('x2: ',x2)  #Newton

print(float(x2))

y =  568.123+1.88*x-0.003*x**2
print(float(y.subs(x,100)))
