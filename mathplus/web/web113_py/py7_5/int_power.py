# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_5_int_power(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = integrate((red_word[0]**x + red_word[1]**x)/red_word[2]**x, x)
    result.append(latex(simplify(s)).replace('log','ln'))
    return result

if __name__ == '__main__':
    red_word = [16,20,4]; #1816956
    for i in p7_5_int_power(red_word):
        print(i)