from sympy import *
x,y = symbols('x y')
##
# g = x*exp(y)-x+y;     
# g = exp(x/y) -x+y;
# g =exp(y)*sin(x)-1*x-x*y;
# g = 12*x**7-7*x**4*y**3+6*x*y**5-14*y**6+25-10;
# g = x**2*y+x*y**2-6;
g = y*cos(x)-x**2-y**2;
##
dydx = -1*  diff(g,x)  / diff(g, y); 
print(simplify(dydx))