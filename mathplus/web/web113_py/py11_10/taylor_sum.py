from sympy import *
import pyperclip #剪贴板

x,n,c = symbols('x n c')
## 泰勒展开的前n项和及误差 ## 阶乘 factorial
x0 = 0.1; x1 = 0.2;
# y = sqrt(x);a=9;n=2;x0=9;x1=9.2;
# y = 1/ (16-x)**(1/4); a = 0; n = 4-1; #R=16 分母那个常数
# y = 1/sqrt(16-x); a=0; n = 4-1; #半径就是题中数
# taylor(2*x/sin(1*x),x,0,'Order',5)
# y = 3*cos(x); a = 13*pi; n = 4; # \left(-1\right)^{n+1}\cdot \frac{3}{\left(2\cdot n\right)!}\cdot \left(x-11\cdot \pi \right)^{2\cdot n}
# y = 1/(1+8*x**3);a = 0; n = 9;  #收敛区间 （-1/2 1/2），2==8**(1/3)
# y = exp(8*x)*log(1-x/2);a = 0; n = 3;
# y = exp(7*x); a = 0; n = 5; #写法是不带化简的(taylor)  R无穷
# y = exp(-x**2/13); an = (-1)**n*x**(2*n+1)/( 13**n*(2*n+1)*n!  )
# y = 7*sec(3*x); a = 0; n = 5;
# y = 2*x / sin(5*x); a = 0; n = 5;
# taylor(2*x/sin(1*x),x,0,'Order',5)
# y = 1/ (27-x)**(1/3); a = 0; n = 4-1; #R = 分母那个数
# y = cos(3*x)/5; a = 0; n = 5; # \frac{1}{5}\cdot \left(-1\right)^n\cdot \frac{\left(3\cdot x\right)^{2\cdot n}}{\left(2\cdot n\right)!}
# y = 4*(1-x)**(-2); a = 0; n = 4; #导数时 系数不带负  6\cdot \left(n+1\right)
# y = 3/x; a = -3; n = 4; # 改3个数字  \left(-3\right)\cdot \frac{\left(x+3\right)^n}{3^{n+1}}
# y = exp(8*x)*log(1-x/1); a = 0; n = 3;
# y = exp(-2*x**2)*cos(3*x); a = 0; n = 5;
# y = x*log(3*x); a = 1; n = 3; x0 = 0.6; x1 = 1.4;
# y = 7*cos(x); a = 9*pi;n = 5; # \left(-1\right)^{n+1}\cdot \frac{7}{\left(2\cdot n\right)!}\cdot \left(x-9\cdot \pi \right)^{2\cdot n}
# y = cos(3*x)/5; a = 0; n = 5; # 半径 无穷 taylor: \frac{1}{5}\cdot \left(-1\right)^n\cdot \frac{\left(3\cdot x\right)^{2\cdot n}}{\left(2\cdot n\right)!}
# y = log(1+2*x); a = 3; n = 3; x0 = 2.7; x1 = 3.3;
# y = log(2*x)/(3*x); a = 1/2; n = 3;
# y = 2*x + exp(-3*x); a = 0; n = 3;
# y = exp(-4*x)*sin(1*x); a = 0; n = 3;
# y = exp(8*x); a = 0; n = 5; #n在那种题里 n-1
# y = exp(3*x**2); a = 0; n = 3; x0 = 0; x1 = 0.2;
# y  = x*exp(-4*x); a = 0; n = 3;
# y = -1*sin(x);a = pi/6; n = 4; x0 = 0; x1 = pi/3;
# y = x*sin(2*x); a = 0; n = 4; x0 = -0.6; x1 = 0.6;
# y = asin(4*x);  a = 0; n = 3;
# y = 15*atan(x); a = 1; n = 3;
# y = acot(x); a = 0; n = 7;
# y = 1*sinh(3*x); a = 0; n = 3; x0 = -1; x1 = -x0;
# y = sqrt(x); a = 9; n = 2; x0 = 9; x1 = 9.2;
y = x**(1/3); a = 64; n = 2; x0 = 63; x1 = 65;
# y = x**(1/3); a = 64; n = 3; x0 = 0.7; x1 =1.3;
# y = 1/(1+x**2); a = 0; n = 7;
# y = 1/ (16-x)**(1/4); a = 0; n = 4-1; #R=16 分母那个常数
# y = 3*x/(1+x); a = 0; n = 5;
# y = 1*x*exp(-x**2); a = 0;n = 10;
# y = sin(x); a = pi/3; n =5;
# y=7/x;a=-4;n=5; # \left(-4\right)\cdot \frac{\left(x+3\right)**n}{3**{n+1}}
## 求前n项和
dy1 = diff(y);
dy2 = diff(dy1);
dy3 = diff(dy2);
dy4 = diff(dy3);
dy5 = diff(dy4);
dy6 = diff(dy5);
dy7 = diff(dy6);
dy8 = diff(dy7);
dy9 = diff(dy8);
fa0 = y.subs(x,a);
fa1 = dy1.subs(x,a);
fa2 = dy2.subs(x,a);
fa3 = dy3.subs(x,a);
fa4 = dy4.subs(x,a);
fa5 = dy5.subs(x,a);
fa6 = dy6.subs(x,a);
fa7 = dy7.subs(x,a);
fa8 = dy8.subs(x,a);
fa9 = dy9.subs(x,a);
n0 = fa0 /factorial(0);
n1 = fa1 /factorial(1)*(x-a);
n2 = fa2 /factorial(2)*(x-a)**2;
n3 = fa3 /factorial(3)*(x-a)**3;
n4 = fa4 /factorial(4)*(x-a)**4;
n5 = fa5 /factorial(5)*(x-a)**5;
n6 = fa6 /factorial(6)*(x-a)**6;
n7 = fa7 /factorial(7)*(x-a)**7;
n8 = fa8 /factorial(8)*(x-a)**8;
n9 = fa9 /factorial(9)*(x-a)**9;
if n == 2:
    tay =  n0 + n1 + n2;
    m = dy3.subs(x,x0);
elif n == 3:
    tay = n0 + n1 + n2 + n3;
    m = dy4.subs(x,x0);
elif n == 4:
    tay = n0 + n1 + n2 + n3 + n4;
    m = dy5.subs(x,x0);
elif n == 5:
    tay = n0 + n1 + n2 + n3 + n4 + n5;
    m = dy6.subs(x,x0);
elif n ==6:
    tay = n0 + n1 + n2 + n3 + n4 + n5 + n6;
    m = dy6.subs(x,x0);
elif n ==7:
    tay = n0 + n1 + n2 + n3 + n4 + n5 + n6 + n7;
    m = dy7.subs(x,x0);
elif n ==8:
    tay = n0 + n1 + n2 + n3 + n4 + n5 + n6 +n7 + n8;
    m = dy8.subs(x,x0);
elif n ==9:
    tay = n0 + n1 + n2 + n3 + n4 + n5 + n6 +n7 + n8 + n9;
    m = dy9.subs(x,x0);

print(tay)
print(dy1)
print(dy2)
print(dy3)
print(dy4)
print(fa0)
print(fa1)
print(fa2)
print(fa3)
print(fa4)

## 误差估计  factorial
rn_max = m/factorial(n+1) * (x1-a)**(n+1);
print('%.8f\n' % abs(rn_max))
pyperclip.copy(float(round(abs(rn_max),8)))
print('误差结果已复制')
print(latex(tay).replace('log','ln'))