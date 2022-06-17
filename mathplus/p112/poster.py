from sympy import *
x = symbols('x')
##
area = 6000;
w = 10;
s = 6;
##
y = (area/x-w*2)*(x-s*2)
##
v = max(solve(diff(y)))
a = (area/v-w*2)*(v-s*2)
print(v,a)