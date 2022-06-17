# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from scipy.integrate import quad


def p10_4_oneloop_cos(red_word):#807879,3
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    r = red_word[0]*cos(red_word[1]*t)
    a = r**2/2
    s = integrate(a,(t,0,pi/red_word[1]))
    #
    result.append(latex(simplify(s)))
    return result

if __name__ == '__main__':
    red_word = [3,7];
    for i in p10_4_oneloop_cos(red_word):
        print(i)
