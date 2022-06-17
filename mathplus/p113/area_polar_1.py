from sympy import *
st = symbols('st')
## parameter
# r = sqrt(7*sin(1*st)); xx = [0, pi/3];
# r = sqrt(7*cos(7*st));#结果都是最前面的系数
# r = sqrt(st); xx = [3/2*pi, 2*pi];
# r = exp(st/2); xx = [pi, 2*pi];
# r = 4-1*sin(1*st); xx = [0*pi, 2*pi];
# r = 1*sin(1*st); xx = [pi/4, 3/4*pi];
# r = 9*(1+cos(st));xx = [0, 2*pi];
# r=cos(11*st);xx = [0, 1/11*pi];
# r = 6*cos(5*st); xx = [0, 2/2/5*pi]; #结果*n n*st的n
# r= 4+1*cos(2*st);  xx = [0, 2*pi];
# r = st**3; xx = [0, pi/2];
## calculation
if len(xx) == 1:
    x0 = -abs(xx); x1 = -x0;
elif len(xx) == 2:
    x0 = xx[0]; x1 = xx[1];
a = integrate(1/2 * r**2, (st, x0, x1));
a = abs(a)
## result
print("%g" % a.evalf())
print(simplify(a))
