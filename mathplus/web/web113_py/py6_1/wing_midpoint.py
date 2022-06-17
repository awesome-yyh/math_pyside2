# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_1_wing_midpoint(red_word):#1817540,13
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    #
    a = red_word[-1]
    y = red_word[1:-1]
    #
    n = 5
    d = a/n
    k = (len(y)-1)/n
    x = np.arange(2, len(y), k)
    ssum = 0
    for i in x:
        ssum += y[int(i)-1]

    s = d * ssum;

    result.append(str(round(s,2)))
    return result

if __name__ == '__main__':
    red_word = [20,6.1,19.9,26.7,29.0,27.1,26.9,23.9,20.6,16.3,8.3,3.3,200];
    for i in p6_1_wing_midpoint(red_word):
        print(i)

