from sympy import *
x = symbols('x')
##
y = (x+1)**4; a = -3;
# y = x**2*exp(2*x);a=-1000000;
# y = 2*x/(x**2-4);a = 3;
# y = (x-1)/x**2; a = 3;
##
# fplot(y)
dy = diff(y); 
ddy = diff(dy); 
pp = solve(ddy);
print('inflection point: ')
print(pp)
print('middle point of inflection point：')
print(simplify(sum(pp)/len(pp)))
if dy.subs(x,a) > 0:
    print('increasing')
else:
    print('decreasing')
if ddy.subs(x,a) > 0:
    print('up')
else:
    print('down')
