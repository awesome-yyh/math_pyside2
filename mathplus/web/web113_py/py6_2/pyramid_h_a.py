# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_2_pyramid_h_a(red_word):#1291713,2
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    h = red_word[0];
    a = red_word[1]; 
    #
    s = h * a**2 * sqrt(3); 

    result.append(latex(s/12))
    return result

if __name__ == '__main__':
    red_word = [5,5];
    for i in p6_2_pyramid_h_a(red_word):
        print(i)
