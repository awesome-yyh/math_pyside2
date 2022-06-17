# 3-diff to int
from sympy import *
x = symbols('x')
##
dddf = x**(-3)+6*x;
# dddf = cos(x);
x0 = 1;
fx0 = -1;
xd0 = 1;
fxd0 = 0;
xdd0 = 1;
fxdd0 = 1;
##
c0 = fxdd0 - integrate(dddf,x).subs(x,xdd0)
ddf = integrate(dddf,x)+c0 
c1 = fxd0 - integrate(ddf,x).subs(x,xd0)
df = integrate(ddf,x)+c1
c2 = fx0 - integrate(df).subs(x,x0)
f = integrate(df,x)+c2
print(simplify(f),'\n',f)