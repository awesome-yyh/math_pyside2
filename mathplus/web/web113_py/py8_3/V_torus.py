# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_torus(red_word):
    red_word = list(map(float,red_word))
    result = []
    x= symbols('x')
    ##
    r = red_word[0];
    d = red_word[1];
    #
    s = r**2*2*d
    #
    result.append(str(int(s))+'*pi^2')
    return result

if __name__ == '__main__':
    red_word = [10,14] #1816145,4
    for i in p8_3_torus(red_word):
        print(i)

