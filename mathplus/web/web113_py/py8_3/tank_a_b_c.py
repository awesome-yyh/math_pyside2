# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_tank_a_b_c(red_word):
    red_word = list(map(float,red_word))
    result = []
    x= symbols('x')
    #
    l = red_word[0];
    w = red_word[1];
    h = red_word[2];
    d = red_word[3];
    ##
    ro = 820;
    a = ro*9.8*d
    b = ro*9.8*d*l*w
    result.append(str(round(a,3)))
    result.append(str(round(b,3)))

    if d < h:
        c = integrate(ro*9.8*x*w,(x,0,d));
    else:
        c = integrate(ro*9.8*x*w,(x,d-h,d));
    #
    result.append(str(round(float(c),3)))
    return result

def p8_3_dam_30du(red_word):
    red_word = list(map(float,red_word))
    result = []
    x= symbols('x')
    #
    t = red_word[0];
    w = red_word[1];
    h = red_word[2];
    ##
    A = sqrt(h**2-(w/2)**2);
    F = 62.5*integrate(sqrt(3)/2*(w+w/A*x)*(A-x),(x,0,A))
    #
    result.append(str(round(float(F))))
    return result

if __name__ == '__main__':
    red_word = [80,40,60] #1816145,4
    for i in p8_3_dam_30du(red_word):
        print(i)

