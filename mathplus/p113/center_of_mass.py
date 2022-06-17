from sympy import *
x = symbols('x')
##
ro = 1;
# aa = [6,4];ro= 2; y1 = aa[1]/aa[0]*x; y2 = 0; xx = [0, aa[0]]; #aa是题中的坐标
# y1 = 2/x; y2 = 0; xx = [5,15];
# y1 = 1*x+0;  y2 = x**2; xx = solve(y1-y2);
# y1 = 4*sqrt(1-x**2/49);y2 = 0; xx = [0, 7];
# y1 = (30-6*x)/5; yxi = 5; y2 =0; xx = [0, yxi]; #y的系数
# y1 = -36+18*x-2*x**2; y2 = 0; xx = solve(y1-y2);
y1 = 3*sin(2*x); y2 = 0;xx = [0, 1/2*pi];
# y1 = 5*sin(pi/1*x); y2 = 0; xx = [0, 1];
# y1 = 7*sqrt(1-x**2/64); y2 = 0; xx = [0, 8];
# y1 = sqrt(x); y2 = 0;xx = [0, 4];
## 
xa = xx[0]; xb = xx[1];
A = integrate(y1-y2,(x,xa,xb));
Mx = ro * integrate(1/2 * (y1**2-y2**2),(x,xa,xb));
My = ro * integrate(x*(y1-y2),(x,xa,xb));
M =ro * A;
xb = My / M;
yb = Mx / M;
##
print(Mx, My, xb, yb)
print(latex(xb).replace('log','ln'))
print(latex(yb).replace('log','ln'))
print('Mx=%g, My=%g, xb=%g, yb=%g'% (Mx,My,xb,yb));