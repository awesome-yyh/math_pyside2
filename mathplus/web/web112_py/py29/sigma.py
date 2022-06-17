# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p29_sum1(red_word):#3806084,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x- red_word[1]
    s = 0
    for i in range(4,9):
        s += f.subs(x,i)
    result.append(str(s))
    return result 

def p29_sum_cos(red_word):#3806076,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = cos(x*pi)*red_word[0]
    s = 0
    for i in range(0,9):
        s += f.subs(x,i)
    result.append(str(s))
    return result 

if __name__ == '__main__':
    red_word = [5]
    for i in p29_sum_cos(red_word):
        print(i)
