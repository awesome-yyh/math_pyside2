# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p31_table39(red_word):#3803449,7
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( sum([-red_word[2], red_word[4], red_word[6]])*2 ))
    result.append('greater')
    result.append(str( sum([-red_word[0], -red_word[2], red_word[4]])*2 ))
    result.append('less than')
    result.append(str( sum([-red_word[1], red_word[3], red_word[5]])*2 ))
    result.append('one cannot say')
    return result 

def p31_dint1(red_word):#3804448,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = 1-x
    result.append(latex( integrate(f,(x,-red_word[1],red_word[0])) ))
    return result 

def p31_fgc(red_word):#3804109,7
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( red_word[-2]*red_word[1]+red_word[-1]*red_word[3] ))
    return result 

if __name__ == '__main__':
    red_word = [10,39,10,16,10,4,5]
    for i in p31_fgc(red_word):
        print(i)
