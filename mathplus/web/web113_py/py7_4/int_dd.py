# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_4_int_dd(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    y = 1/((x+red_word[0])**2*(x-red_word[1]))
    s = integrate(y,x)
    result.append(latex(simplify(s)).replace('log','ln'))
    return result

def p7_4_int_log2(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    y = red_word[0]*log(x**2-x+red_word[1])
    s = integrate(y,x)
    result.append(latex(simplify(s)).replace('log','ln'))
    return result

if __name__ == '__main__':
    red_word = [5,12];
    for i in p7_4_int_log2(red_word):
        print(i)