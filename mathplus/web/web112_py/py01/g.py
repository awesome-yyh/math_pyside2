# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_gsqrt(red_word):#3799234,1
    red_word = list(map(int,red_word))
    x,s0 = symbols('x s0')
    result = []
    # 
    result.append('3')
    result.append('2')
    result.append('2 3')
    result.append('x-3')
    f = simplify(2*sqrt(s0*(x-3)-(x-3)**2))
    f = latex(f).replace('s0',str(red_word[0]))
    result.append(str(f))
    #
    return result

if __name__ == '__main__':
    red_word = [ 5];
    for i in p01_gsqrt(red_word):
        print(i)