from sympy import *
x,y = symbols('x y')
##
xy = 80000;
div = 3; #分成几份
##
z = (div+1)*x + 2*y;
z = z.subs(y,xy/x);
x0 = max(solve(diff(z)));
y0 = xy/x0;
lengh = z.subs(x,x0);
if x0>y0:
    print('lengh = ', simplify(x0))
    print('width = ', simplify(y0))
else:
    print('lenghn = ', simplify(y0))
    print('width = ', simplify(x0))

print('sum lengh = ', simplify(lengh))
print('unit is "feet", if 250000 square feet')
