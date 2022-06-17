from sympy import *
st = symbols('st')
## parameter
n = 1; #n*st
# xi=5;r1 = xi+1*cos(st);r2 = xi-1*cos(st); flag = 0;#之和改之差，（-常数）
# r1 = sin(st); r2 = 1-sin(st);flag = 1;
# r1 = sin(n*st); r2 = cos(n*st); flag = 1;
r1 = 4+2*sin(n*st); r2 = 4+2*cos(n*st); flag = 0;
# r1 = 30*sin(n*st); r2 = 10+10*sin(n*st);用1i2o求
# r1 = cos(st); r2 = sin(st); 用 area_polar_21 求
# r1 = sqrt(3)/3*cos(st);r2 = sin(st);用area_polar_21
##
if flag:
    x1 = solve(r1/r2-1);
    a = pi/x1[0]*2*integrate(1/2*r1**2,(st,0,x1[0]))
else:
    x0 = solve(r1-r2);
    x1 = x0[0]+pi/n;
    a = 2*integrate(1/2*r2**2,(st, x0[0],x1))
## result
a = abs(a)
print("%g" % a.evalf())
print(simplify(a))
