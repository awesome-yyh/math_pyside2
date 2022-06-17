# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from math import ceil

def p7_7_simpson_large_n(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    #
    y = red_word[0]*exp(x**2);x0 = 0;x1 = 1;err = red_word[1];
    ##
    dy1 = diff(y);
    dy2 = diff(dy1);
    dy3 = diff(dy2);
    dy4 = diff(dy3);
    k = dy4.subs(x, 1);
    ab = (x1-x0)**5;
    n = (k*ab/err/180)**(1/4);
    #
    result.append(str(ceil(float(n))))
    return result

if __name__ == '__main__':
    red_word = [7,0.00001]; #1816754
    for i in p7_7_simpson_large_n(red_word):
        print(i)