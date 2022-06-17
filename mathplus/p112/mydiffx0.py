from sympy import *
x,t = symbols('x t')
# f = integrate(sqrt(1+3*t),(t,2,2*x)); a = 8;
# f =(x**3+2*x-1)**4; a = 0;
# f = x**2+12*x**(1/2); a = 4;
# f = 4*x**2+5*x+170; a = 3;
# f = log(x**2+3); a = 2;
# f = 4*cos(pi/6*x);a=11;
# f = 4*sin(pi/3*x);a=4;
# f = 0.002*x**2+7*x+5000;a=1000;             
# f = 20*x**(2/3); a=8;
# f = sqrt((120-20*x)**2+(80-10*x)**2);a=2;
# f = 96+80*x-16*x**2;f=diff(f); a=2;
# f=x/(3*x+2);a=2/3;
# f=2*atan(3*x);a=1;
# f=6*x**(5/3)-12*x**(1/3);a=8;
# f=sin(x)*(tan(x)-cos(x));a=pi/4;
f = 41*x-16*x**2;a=1
##
print(simplify(diff(f).subs(x,a)))