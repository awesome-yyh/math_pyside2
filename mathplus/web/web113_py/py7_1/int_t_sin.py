# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_1_int_t_sin(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = integrate(red_word[0]*x*sin(red_word[1]*x), (x, 0, pi))
    result.append(latex(simplify(s)))
    return result

if __name__ == '__main__':
    red_word = [8,17]
    for i in p7_1_int_t_sin(red_word):
        print(i)
