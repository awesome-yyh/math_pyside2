# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_domain3d2(red_word):#3799116,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    f = x**2+red_word[2]*x- red_word[3]
    #
    return p01_domain2(f,x,result)

def p01_domain2(f,x,result):
    dom = '\\left(-\\infty ,s0\\right),\\left(s0,s1\\right),\\left(s1,\\infty \\right)'
    ss = solve(f)
    result.append( dom.replace('s0',str(ss[0])).replace('s1',str(ss[1])) )
    return result

if __name__ == '__main__':
    red_word = [ 5,3,2,24];
    for i in p01_domain3d2(red_word):
        print(i)