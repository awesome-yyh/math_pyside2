from sympy import *
st = symbols('st')
## parameter
# r1 = sqrt(32*cos(2*st));r2 = 4;xx = solve(r1-r2);#结果*2
# r1 = 2*sin(3*st); r2 = 1; xx = solve(r1-r2); #结果变加
r1 = 15*sin(st); r2 = 5+5*sin(st);xx = solve(r1-r2);
# r1 = 2*cos(st); r2 = 1;xx = solve(r1-r2);
## calculation
if len(xx) == 1:
    x0 =xx;
    a = 4*int(1/2*r1**2,0, x0);
elif len(xx) == 2:
    x0 = xx[0]; x1 = xx[1];
    a = integrate(1/2 * (r1**2 - r2**2), (st, x0, x1));
a = abs(a)
## result
print("%g" % a.evalf())
print(simplify(a))
