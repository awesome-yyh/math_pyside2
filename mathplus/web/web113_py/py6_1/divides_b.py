# 返回元素为字符串的list
# 参数是[100,800]的list
import numpy as np
from sympy import *

def p6_1_divides_b(red_word):
    red_word = list(map(float,red_word))
    result = []
    x,b = symbols('x b')
    ##
    y1 = red_word[0] * x**2;  #写x = .. y1 y2顺序不能换
    y2 = red_word[1];
    ##
    xx = solve(y1-y2);
    x1 = xx[0]; x2 = xx[1];
    b = solve(integrate(sqrt(x)-0, (x,0, b)) - integrate(sqrt(x), (x,b, y2)));
    #
    result.append(str(round(float(b[0]),2)))
    return result

if __name__ == '__main__':
    red_word = [36,9] #1816130,2
    for i in p6_1_divides_b(red_word):
        print(i)
