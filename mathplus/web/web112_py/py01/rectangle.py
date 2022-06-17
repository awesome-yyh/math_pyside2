# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_rectangle(red_word):#3798614,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    A = 'L\\left(aa-L\\right)'
    result.append(A.replace('aa',str(red_word[0]/2)))
    #
    dom = '\\left(s0,s1\\right)'
    result.append( dom.replace('s0',str(red_word[0]/4)).replace('s1',str(red_word[0]/2)) )
    return result

    solve(Ax)
    #
    return result

if __name__ == '__main__':
    red_word = [24];
    for i in p01_rectangle(red_word):
        print(i)