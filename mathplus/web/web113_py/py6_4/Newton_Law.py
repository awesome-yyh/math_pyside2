# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_Newton_Law(red_word):
    red_word = list(map(float,red_word))
    result = []
    H = symbols('H')
    #
    m = red_word[0];
    h = red_word[1];
    ## 计算
    h = h * 1000;
    G = 6.67 * 10**(-11);
    M = 5.98 * 10**24;
    r = 6.37 * 10**6;
    f = G * M * m / (r + H)**2;
    w = integrate(f,(H, 0, h));
    #
    result.append(str(round(w,3)))
    return result

if __name__ == '__main__':
    red_word = [1600,900] #657132,2
    for i in p6_4_Newton_Law(red_word):
        print(i)
