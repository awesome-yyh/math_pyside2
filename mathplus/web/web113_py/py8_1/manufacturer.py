# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from scipy.optimize import fsolve, root

def p8_1_manufacturer(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    ##
    s = 'NIntegrate[Sqrt[1 + (Pi*Cos[Pi*x/rw1]/rw1)^2], {x, 0, rw0}]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    #
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [40,41,25]; #1816794,3
    for i in p8_1_telephone(red_word):
        print(i)