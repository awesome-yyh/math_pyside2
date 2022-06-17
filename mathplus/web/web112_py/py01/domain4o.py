# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_domain4o_d(red_word):#3798734,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    f = x+1/x
    g = (x+red_word[0])/(x+red_word[1])
    #
    return p01_domain4o(f,g,x,result,red_word)

def p01_domain4o(f,g,x,result, red_word):

    dom1 = '\\left(-\\infty ,-'+str(red_word[0])+'\\right),\\left(-'+str(red_word[0])+',-2\\right),\\left(-2,\\infty \\right)'
    dom2 = '\\left(-\\infty ,-1\\right),\\left(-1,0\\right),\\left(0,\\infty \\right)'
    dom3 = '\\left(-\\infty ,0\\right),\\left(0,\\infty \\right)'
    d4 = solve(red_word[1]+(x+red_word[0])/(x+red_word[1]))
    dom4 = '\\left(-\\infty ,'+str(d4[0])+'\\right),\\left('+str(d4[0])+',-2\\right),\\left(-2,\\infty \\right)'
    
    result.append(latex(f.subs(x,g)))
    result.append(dom1)
    result.append(latex(g.subs(x,f)))
    result.append(dom2)
    result.append(latex(f.subs(x,f)))
    result.append(dom3)
    result.append(latex(g.subs(x,g)))
    result.append(dom4)
    return result

if __name__ == '__main__':
    red_word = [ 14,2];
    for i in p01_domain4o_d(red_word):
        print(i)