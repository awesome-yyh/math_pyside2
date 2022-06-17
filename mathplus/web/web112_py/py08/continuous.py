# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p08_continuous2(red_word):#3802700,5
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( (2*x-1).subs(x, red_word[0]) ))
    return result 

def p08_continuous_fg(red_word):#3802708,5
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( red_word[3]/(3+ red_word[1]) ))
    return result 

def p08_continuous4(red_word):#3803008,15
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append('continuous')
    f = x**4+x- red_word[0]
    result.append(str( f.subs(x, red_word[1]) ))
    result.append(str( f.subs(x, red_word[2]) ))
    result.append('0')
    result.append('0')
    result.append('root')
    return result 

def p08_continuous_exp(red_word):#3802542,8
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = exp(x)-red_word[0]+red_word[1]*x
    result.append(str( f.subs(x, 0) ))
    result.append(str( f.subs(x, 1) ))
    result.append('f(0)')
    result.append('f(1)')
    return result 

if __name__ == '__main__':
    red_word = [4,3,4,3,4,3,4,3]; 
    for i in p08_continuous_exp(red_word):
        print(i)