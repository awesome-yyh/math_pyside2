# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from math import ceil

def p7_7_g_TM(red_word):
    red_word = list(map(float,red_word))
    result = []
    #
    
    #
    result.append(r'-\frac{1}{x^2}')
    result.append(r'\frac{2}{x^3}')
    result.append(r'\frac{2}{x^3}')
    result.append('2')
    result.append('1')
    result.append('1')
    n = 1/sqrt(red_word[0]*6)
    result.append(str(ceil(n)))
    result.append('1')
    result.append('24')
    s = 1/sqrt(12*red_word[0])
    result.append(str(round(s,1)))
    return result

if __name__ == '__main__':
    red_word = [0.00009,0.00009,0.00009,0.00009,0.00009,0.00009,0.00009]
    for i in p7_7_g_TM(red_word):
        print(i)