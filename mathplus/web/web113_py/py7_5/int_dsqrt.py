# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_5_int_dsqrt(red_word):#1817074,1
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[rw0/(Sqrt[x] + x*Sqrt[x]), x]'
    s = s.replace('rw0',str(red_word[0]))
    result.append(s)
    return result

def p7_5_int_dxsqrtd(red_word):#1816564,2
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[1/(x*Sqrt[rw0*x+rw1]), x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [ 8,9]; 
    for i in p7_5_int_dxsqrt(red_word):
        print(i)