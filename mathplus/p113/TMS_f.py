from sympy import *
import numpy as np
x = symbols('x')
# y = exp(4*sqrt(x))*sin(5*x); x0 = 0; x1 = 4; n = 8;
# y = 3*x*exp(x); x0 = 0; x1 = 1; n = 5*2*2;
# y = sqrt(3*x)*exp(-6*x); x0 = 0; x1 = 1; n = 10;
# y = sqrt(1+sqrt(x)); x0 = 0; x1 = 4; n = 8;
# y = 19/sqrt(x); x0 = 1; x1 = 4; n = 12;
# y = x**2*sin(x); x0 = 0; x1 = pi; n = 12;
# y = 9*sin(exp(1*x/2)); x0 = 0; x1 = 1/2; n = 8;
# y = 3*sin(x); x0 = 0; x1 = pi; n = 10; ee =  0.00001;
# y = 8*sin(x**2/1); x0 = 0; x1 = 1/2; n = 4;
# y = 9*cos(x**2); x0 = 0; x1 = 1; n = 4; ee =  0.0001;
# y = 7*cos(sqrt(5*x)); x0 = 0; x1 = 4; n = 10;
# y = 2*cos(5*x)/x; x0 = 1; x1 = 5; n = 8;
# y = 8*cos(8*pi*x); x0 = 0; x1 = 20; n = 10;
# y = 1*(5+x**2)**(1/4); x0 = 0; x1 = 2; n = 8;
# y = 1/(8+x**5); x0 = 0; x1 = 3; n = 6;
# y = 9/(1+t**2+t**4); x0 = 0; x1 = 3; n = 6;
# y = 9/x**2; x0 = 1; x1 = 2; n = 5*2*2;
# y = 30*x**4; x0 = 0; x1 = 2; n = 6*2;
# y = 1/x; x0 = 1; x1 = 3; n = 4; ee = 0.01;
# y = (x+4)*(x-14)**2;x0=-3;x1=15;n=6;
# y = 3+4*x**2;x0=-1;x1=2;n=3;
# y = sin(x**2); x0 = 0; x1 = 1; n = 4; ee = 0.001;
# y = sin(x)/x;x0 = 0; x1 = 1; n = 4; ee = 10**(-6);
y = 4+2*x**2;x0=-1;x1=2;n=6;ee = 10**(-6);
dy2 = diff(diff(y))
dy4 = diff(diff(dy2))
## 公共部分
delta = (x1-x0)/n;
inte = integrate(y, (x,x0, x1));
print('inte = %f' % inte)
ly = lambdify(x,y)
## Trapezoidal Rule
xt = np.linspace(x0, x1, n+1)
xtp = np.linspace(2, len(xt)-1, n-1)
tsum = 0
t_rule = [ly(x0)]
for i in xtp:
    tsum += ly(xt[int(i-1)])
    t_rule.append(ly(xt[int(i-1)])*2)
tn = delta * 1/2 * ly(x0) + 2*tsum + ly(x1);

print('t rule delta: ', delta*1/2)
t_rule.append(ly(x1))
print(t_rule)

te = inte - tn;
print('t = %f  te = %f\n' % (tn, te))
## Midpoint Rule
xm = np.linspace(x0+delta/2, x1-delta/2, n)
mn = delta * sum(ly(xm));
me = inte - mn;
print('m = %f  me = %f\n' % (mn, me))
## Simpsons Rule
xs = np.linspace(x0, x1, n+1)
f4 = np.linspace(2, n, (n-2)/2+1)
f2 = np.linspace(3, n-1, (n-4)/2+1)
ssum4 = 0
s_rule = [ly(x0)]
for i in f4:
    ssum4 += ly(xs[int(i-1)])
    s_rule.append(ly(xs[int(i-1)])*4)
ssum2 = 0
for i in f2:
    ssum2 += ly(xs[int(i-1)])
    s_rule.append(ly(xs[int(i-1)])*2)
sn = delta * 1/3 * (ly(x0) + 4*ssum4 + 2*ssum2 + ly(x1));

print('s rule delta: ', delta*1/3)
s_rule.append(ly(x1))
print(s_rule)

se = inte - sn;
print('s = %f  se = %f\n' % (sn, se))
