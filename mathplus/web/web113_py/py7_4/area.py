# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_4_area(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    s = 'Integrate[(x^2 + rw1)/(rw2*x - x^2), {x, 1, rw0}]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    s = s.replace('rw2',str(red_word[2]))
    #
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [2,1,3];
    for i in p7_4_area(red_word):
        print(i)