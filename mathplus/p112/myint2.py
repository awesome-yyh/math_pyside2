# second diff to int
from sympy import *
import pyperclip #剪贴板

x = symbols('x')
##
# ddf = 5*exp(x)-6*cos(x);
# ddf = 16+18*x+36*x**2;
# ddf = -2*sin(x);
# ddf = 18/sqrt(x);
ddf = x**2-3*x+8
x0 =  0;
fx0 = 0;
xd0 = 1;
fxd0 = 20;
v0 = pi/6;
##
c1 = fxd0 - integrate(ddf,x).subs(x,xd0)
df = integrate(ddf,x)+c1
c2 = fx0 - integrate(df,x).subs(x,x0)
f = integrate(df,x)+c2
fv0 = f.subs(x,v0)
print(simplify(f),'\n',f)
pyperclip.copy(latex(simplify(f)).replace('x','t'))
print(simplify(fv0),'\n',fv0)

print(f.subs(x,1))