# 返回元素为字符串的list
# 参数是[100,800]的list
import numpy as np
from sympy import *

def p6_1_area_3(red_word):
    result = []
    x = symbols('x')
    ##
    # y1 = 1*x**2; y2 = 8*x**2; y3 = 3-2*x;
    y1 = 4/x; y2 = 16*x; y3 = x/9;
    ##
    x12 = solve(y1-y2);
    x12 = max(x12);
    x13 = solve(y1-y3);
    x13 = max(x13);
    x23 = solve(y2-y3);
    x23 = max(x23);
    xxx = [x12, x13, x23];
    if(min(xxx) < 0):
        printegrate('查看一下 让xxx都大于0')
    xmax = max(xxx);
    if xmax == x12:
        s = integrateegrate(y3-y2, (x,x23,x13)) + integrate(y1-y2, (x,x13,x12));
    elif xmax == x13:
        s = integrate(y2-y3, (x,x23,x12)) + integrate(y1-y3, (x,x12,x13));
    else:
        s = integrate(y1-y3, (x,x13,x12)) + integrate(y2-y3, (x,x12,x23));
    #
    result.append(str(abs(s)))
    result.append(str(float(s)))
    return result

if __name__ == '__main__':
    red_word = [0] #1816130,2
    for i in p6_1_area_3(red_word):
        print(i)
