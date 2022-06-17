# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from math import ceil

def p7_7_tm_cos2(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    #
    y = red_word[0]*cos(x**2); x0 = 0; x1 = 1; n = 4;
    return TM_f(y,x0,x1,n)

def TM_f(y,x0,x1,n):
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
    #
    result.append(str(round(float(tn),6)))
    result.append(str(round(float(mn),6)))
    result.append('under')
    result.append('over')
    result.append(str(round(float(tn),6)))
    result.append(str(round(float(mn),6))) 
    return result

if __name__ == '__main__':
    red_word = [11]; #1386798,1
    for i in p7_7_tm_cos2(red_word):
        print(i)
