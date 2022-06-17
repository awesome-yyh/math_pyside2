from sympy import *
x = symbols('x')
# y = x**5-15*x**3-0*x+50;
# y = 30*2*x+9000/x*(90+30);
# y = (x-12)*(6000/x-20);
# y=2000/x+10*x**2;
# y = (6000/x-20)*(x-12)
# y=(8-2*x)*(5-2*x)*x;
# y=90*x+30*2*4000/x+30*x;
# y=x*4/3*(3-x);
# y = "120*x+60000/x";
# y = core.add.Add(a)
# y = x*(6000-2*x)/3;
# y = 2*sin(x)+cos(x)
# y = sqrt((15*x)**2+(20*x)**2)
# y = 2*x+80000/x
# y= x**3-9*x**2-21*x+9
y = x**3-6*x**2+5
##
v = solve(diff(y))
print(v)
print(float(v[0]))
print(float(v[1]))
print(float(v[2]))