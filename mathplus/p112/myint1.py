## 1 diff to int
from sympy import *
import pyperclip #剪贴板

x = symbols('x')
# df = 15*x**2-6*x;
# df = 1.64-0.002*x
# df = 4*x+2/x**2;
# df = (x+1)/sqrt(x);
# df = 1/(1+x**2)-1/x;
# df = 450.266*exp(1.12567*x)
df = 1/sqrt(1-x**2)
df = 2*x+3*x**1.3
x0 = 1/2;
fx0 = 4;
x1 = 3;
##
c = fx0 - integrate(df,x).subs(x,x0)
f = integrate(df,x)+c
print(simplify(f))
print(simplify(integrate(df,x).subs(x,x0)))
pyperclip.copy(latex(simplify(f)).replace('log','ln'))
# print(f.subs(x,x1))