# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_1_midpoint(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    at = red_word[0]
    y = [0]+red_word[1:]+[0]
    n = 4
    x = np.linspace(1, len(y)-2, n)
    d = at * 2;
    ssum = 0
    for i in x:
        ssum += y[int(i)]

    s = d * ssum;

    result.append(str(s))
    return result

def p6_1_point_tri(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    ##
    x1 = red_word[0]
    y1 = red_word[1]
    x2 = red_word[2]
    y2 = red_word[3]
    x3 = red_word[4]
    y3 = red_word[5]
    #
    a = sqrt((x1-x2)**2 + (y1-y2)**2)
    b = sqrt((x1-x3)**2 + (y1-y3)**2)
    c = sqrt((x3-x2)**2 + (y3-y2)**2)
    s = 1/2 * (a+b+c);
    S = sqrt(s*(s-a)*(s-b)*(s-c))
    #
    result.append(str(round(float(S),2)))
    return result

if __name__ == '__main__':
    red_word = [0,0,6,4,-1,8];
    for i in p6_1_point_tri(red_word):
        print(i)

