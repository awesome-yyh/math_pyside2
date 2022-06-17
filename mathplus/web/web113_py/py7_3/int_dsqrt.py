# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_3_int_dsqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    #
    s = 'Integrate[1/Sqrt[t^2 - rw0 *t + rw1 ], t]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    #
    result.append(s)
    return result

def p7_3_int_sqrtd(red_word): #1817280, 1
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    #
    s = 'Integrate[Sqrt[x^2 - rw0]/x^4, x]'
    s = s.replace('rw0',str(red_word[0]))    
    #
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [9]
    for i in p7_3_int_sqrtd(red_word):
        print(i)
