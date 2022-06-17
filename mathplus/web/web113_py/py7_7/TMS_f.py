# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from math import ceil

def p7_7_TMS_none():
    x = symbols('x')
    #
    # y = (1+x**3)**(1/4);x0=0; x1 = 2; n = 8;
    # y = cos(sqrt(x)); x0 = 0; x1 = 4; n = 10;
    return TMS_f(y,x0,x1,n)

def p7_7_tms_t_fu(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = (red_word[3]+x**red_word[4])**(1/red_word[2]);
    x0=red_word[1]; x1 = red_word[0]; n = red_word[5];
    return TMS_f(y,x0,x1,n)

def p7_7_TMS_f5(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = 1/(red_word[0]+x**5); x0 = 0; x1 = 3; n = 6;
    return TMS_f(y,x0,x1,n)

def p7_7_TMS_flog(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = red_word[0]*log(x**3+red_word[1]); x0 = 4; x1 = 6; n = 10;
    return TMS_f(y,x0,x1,n)

def p7_7_TMS_flogd(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = red_word[0]*log(x)/(1+x); x0 = 1; x1 = 2; n = 10;
    return TMS_f(y,x0,x1,n)

def p7_7_TMS_sqrtsqrt(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = sqrt(red_word[0]+sqrt(x)); x0 = 0; x1 = 4; n = 8;
    return TMS_f(y,x0,x1,n)

def p7_7_TMS_sqrtexp(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = sqrt(red_word[0]*x)*exp(-red_word[1]*x); x0 = 0; x1 = 1; n = 10;
    return TMS_f(y,x0,x1,n)

def p7_7_TMS_cosd(red_word):#1816426,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = red_word[0]*cos(red_word[1]*x)/x; x0 = 1; x1 = 5; n = 8;
    return TMS_f(y,x0,x1,n)

def p7_7_s_mnexp(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    #
    y = exp(x**2);x0=0; x1=red_word[1];n=red_word[0];
    s = TMS_f(y,x0,x1,n)
    return [s[1]]


def p7_7_t_cossqrt(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = red_word[0]*cos(sqrt(red_word[1]*x)); x0 = 0; x1 = 4; n = 10;
    return TMS_f(y,x0,x1,n)

def p7_7_t_sinexp(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    #
    y = red_word[1]*sin(exp(red_word[2]*x)); x0 = 0; x1 = red_word[0]; n = 8;
    return TMS_f(y,x0,x1,n)

def TMS_f(y,x0,x1,n):
    result = []
    x = symbols('x')
    #
    ## 公共部分
    delta = (x1-x0)/n;
    ## Trapezoidal Rule
    xt = np.arange(x0,x1+delta,delta)
    xtp = np.arange(2,len(xt),1)
    sxtp = 0
    for i in xtp:
        sxtp += y.subs(x,xt[i-1])
    tn = delta * 1/2 * (y.subs(x,x0) + 2* sxtp+ y.subs(x,x1));
    ## Midpoint Rule
    xm = np.arange(x0+delta/2, x1+delta/2,delta)
    sxm = 0
    for i in xm:
        sxm += y.subs(x,i)
    mn = delta * sxm;
    ## Simpsons Rule
    xs = np.arange(x0,x1+delta,delta)
    lens = len(xs);
    f4 = np.arange(2,lens+1,2)
    f2 = np.arange(3,lens,2)
    sxsf4 = 0
    for i in f4:
        sxsf4 +=  y.subs(x,xs[i-1])
    sxsf2 = 0
    for i in f2:
        sxsf2 += y.subs(x,xs[i-1])
    sn = delta * 1/3 * (y.subs(x,xs[0]) + 4*sxsf4 + 2*sxsf2 + y.subs(x,xs[lens-1]));
    #
    result.append(str(round(float(tn),6)))
    result.append(str(round(float(mn),6)))
    result.append(str(round(float(sn),6)))
    return result

if __name__ == '__main__':
    red_word = [2,0,4,1,3,8]; #1817527
    # for i in p7_7_tms_t_fu(red_word):
    for i in p7_7_TMS_none():
        print(i)

        