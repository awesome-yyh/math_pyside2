from sympy import *
x, c = symbols('x c')
## parameter
# y1 = x**3-20*x;y2=x**2;xxx = solve(y1-y2);
# y1 = 17*log(x);y2 = x*log(x);xxx = solve(y1-y2);
# y1 = x**2-6*x; y2 = 4*x+7; xxx = solve(y1-y2);
# y1 = 3*x-x**2; y2 = -7*x;xxx = solve(y1-y2);
y1 = 5*x**2; y2 = 0+10*x-5*x**2; xxx = solve(y1-y2);
# y1 = 2*x**2; y2 = 1-4*x;xxx = solve(y1-y2);xxx = [0, 1/5];
# y1 = x**2; y2 = 7/(x**2+6); xxx = solve(y1-y2); xxx = [xxx[0], xxx[1]];#xxx = [-1 1];
# y1 = 5-5*x**2; y2 = 5*x**2-5;xxx = solve(y1-y2);#xxx = [-4, -1]; #分段
# y1 = x+2; y2 = 1*x**2-10; xxx = solve(y1-y2);
# y1 = 1*x+2; y2 = x**2-4;xxx = solve(y1-y2);#xxx = [-1, 2];
# y1 = 2*x; y2 = 2*x**3; xxx = solve(y1-y2);
# y1 = 1*x+5; y2 = 12-x**2; xxx = [-1, 2];
# y1 = 7/x; y2 = 7/x**2; xxx = solve(y1-y2); xxx = [xxx[0], 3];
# xi = 6; y1 = xi/x; y2 = xi/x**2; xxx = solve(y1-y2); xxx = [1, 7];
# y1 = 3*x**2; y2 = -12*x-3*x**2;xxx = solve(y1-y2);
# y1 = 6*sin(x) + sin(6*x); y2 = 0; xxx = [0, pi];
# y1 = -4*x**2; y2 = -16*x+4*x**2;xxx = solve(y1-y2); #xxx = [1 7];
# y1 = 3*(x/2)**2 - (x/2)**4; y2 = 0; xxx = [2*sqrt(2), 2*sqrt(3)];
# y1 = 6*x-x**2; y2 = 2*x;xxx = solve(y1-y2);
# y1 = sqrt(x);y2=x**3;xxx = [0, 1];
## calculation  
if len(xxx) == 3:
    x1 = xxx[0]; x2 = xxx[1]; x3 = xxx[2];
    s = integrate(y1-y2, (x, x1, x2)) + integrate(y2-y1,(x, x2, x3));
elif len(xxx) == 2:
    x1 = xxx[0]; x2 = xxx[1];
    s = integrate(y1-y2, (x, x1, x2));
s = abs(s)
## result
print("%g" % s.evalf())
print(simplify(s))
