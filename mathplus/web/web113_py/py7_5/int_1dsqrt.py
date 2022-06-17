# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_5_int_1dsqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[1/Sqrt[rw0*y^2 - rw1*y - rw2], y]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    s = s.replace('rw2',str(red_word[2]))
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [25,20,21]; #1816954
    for i in p7_5_int_1dsqrt(red_word):
        print(i)