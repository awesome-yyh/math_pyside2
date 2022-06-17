# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_5_int_dx2sqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[rw0/(x^2*Sqrt[rw1*x^2 - 1]), x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [17,16]; #1817489
    for i in p7_5_int_dx2sqrt(red_word):
        print(i)