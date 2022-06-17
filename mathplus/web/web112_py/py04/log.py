# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p04_log(red_word):#3799445,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str(float(log(red_word[0])/log(2))))
    result.append(str(float(log(2)/log(red_word[1]))))
    return result

def p04_logadd(red_word):#3799338,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(latex(log(red_word[0]*red_word[2]**red_word[1])).replace('log','ln'))

    return result

if __name__ == '__main__':
    red_word = [7,2,3]; 
    for i in p04_logadd(red_word):
        print(i)