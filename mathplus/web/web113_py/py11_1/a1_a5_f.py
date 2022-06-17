# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from scipy.integrate import quad


def p11_1_a1_5_f1(red_word):#807879,3
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    a1 = red_word[0]
    a2 = red_word[1]*a1- red_word[2]
    a3 = red_word[1]*a2- red_word[2]
    a4 = red_word[1]*a3- red_word[2]
    a5 = red_word[1]*a4- red_word[2]
    
    #
    result.append(str(a1))
    result.append(str(a2))
    result.append(str(a3))
    result.append(str(a4))
    result.append(str(a5))
    return result

if __name__ == '__main__':
    red_word = [5,2,4];
    for i in p11_1_a1_5_f1(red_word):
        print(i)
