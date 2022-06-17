# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_3_int_x_sqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = 'Integrate[rw0*x*Sqrt[x^2 + rw1], {x, 0, 1}]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    #
    result.append(s)
    return result

def p7_3_int_x_d32(red_word): #1816637,3
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = 'Integrate[x^2/(rw0 + rw1*x - rw2*x^2)^(3/2), x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    s = s.replace('rw2',str(red_word[2]))
    #
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [3,4,4]
    for i in p7_3_int_x_d32(red_word):
        print(i)
