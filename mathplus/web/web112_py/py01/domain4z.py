# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_domain4z_sqrt(red_word):#3799328,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    f = sqrt(red_word[0]-x)
    g = sqrt(x**2- red_word[1])
    #
    return p01_domain2(f,g,x,result)

def p01_domain2(f,g,x,result):
    dom = '\\left(-\\infty ,g0\\right],\\left[g1,s0\\right]'
    dom4 = '\\left(-\\infty ,g0\\right),\\left(g1,s0\\right]'
    ssf = solve(f)
    ssg = solve(g)
    dom = dom.replace('g0',str(ssg[0])).replace('g1',str(ssg[1])).replace('s0',str(ssf[0]))
    dom4 = dom4.replace('g0',str(ssg[0])).replace('g1',str(ssg[1])).replace('s0',str(ssf[0]))
    result.append(latex(f+g))
    result.append(dom)
    result.append(latex(f-g))
    result.append(dom)
    result.append(latex(f*g))
    result.append(dom)
    result.append(latex(f/g))
    result.append(dom4)
    return result

if __name__ == '__main__':
    red_word = [5,4];
    for i in p01_domain4z_sqrt(red_word):
        print(i)