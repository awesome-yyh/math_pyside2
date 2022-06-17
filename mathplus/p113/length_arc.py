from sympy import *
x, t = symbols('x t')
##
# y = 1/2*x**2; xx = [-3, 3];
# y = 3*x**2; xx = [48, 192];
# y = 3*x-2; xx = [-1, 2];
# y = x**4/8+1/(4*x**2);xx=[1, 4];
# y = 4/5*x**(3/2); xx = [0, 100];
# y = log(2-2*x**2); xx = [0, 3/4];
# y = log(cos(x)); xx = [0, pi/4];
# y = log(sin(x)); xx = [pi/2, 2/3*pi];
y = 5/6*x**(6/5) - 5/16*x**(4/5); xx = [2,4];
# y = sqrt(4*(x+4)**3); xx = [0, 2];
# y = 3/5*x**(3/2); xx = [0, 150];
# y = x**5/10 + 1/(6*x**3);xx = [1,2];
# y = 1/3*(x**2-2)**(3/2);xx=[2, 3];
# y = integrate(,(t,pi/4,x));xx=[pi/4, 2/3*pi];
# y =sqrt(9*sin(x)**2-1);xx=[pi/4, 2/3*pi];
## 
x0 = xx[0];x1 = xx[1];
dy = diff(y);
dyy = 1 + dy**2;
dyy = dyy.subs(x, t);
u = dyy**(1/2);
##
print('integral factor: ')
print(simplify(u))
s = integrate(u, (t,x0, x1));
s = abs(s)
print('result: ')
print("%g" % s.evalf())
print(simplify(s))
