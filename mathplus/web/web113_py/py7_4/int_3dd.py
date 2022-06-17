# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_4_int_3dd(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[(rw0*x^3 + rw1*x^2 + rw2*x + rw3)/((x^2 + 1)*(x^2 + rw4)), x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    s = s.replace('rw2',str(red_word[2]))
    s = s.replace('rw3',str(red_word[3]))
    s = s.replace('rw4',str(red_word[4]))
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [3,7,15,7,5];
    for i in p7_4_int_3dd(red_word):
        print(i)