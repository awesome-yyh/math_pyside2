# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p04_solve_e(red_word):#3799080,4
    result = []
    a = '\\frac{\\left(s0-\\ln \\left(s1\\right)\\right)}{4}'
    b = '\\frac{\\left(e^s3+s2\\right)}{3}'
    result.append( a.replace('s0',str(red_word[0])).replace('s1',str(red_word[1])))
    result.append( b.replace('s2',str(red_word[2])).replace('s3',str(red_word[3])) )
    return result

if __name__ == '__main__':
    red_word = [9,2,19,5];
    for i in p04_solve_e(red_word):
        print(i)