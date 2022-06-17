# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_1_int_cosh(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    f = red_word[0]*x*cosh(x)
    s = integrate(f,(x,0,1))
    #
    result.append(latex(simplify(s)))
    print(latex(simplify(s)))
    return result

if __name__ == '__main__':
    red_word = [5]
    for i in p7_1_int_cosh(red_word):
        print(i)
