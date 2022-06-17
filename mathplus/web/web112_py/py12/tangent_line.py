# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p12_tangent_line(red_word):#3802582,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*exp(x)+x
    df = diff(f)
    tan = df.subs(x,0)*(x)+red_word[0]
    result.append(latex( tan ))
    return result 

def p12_diffgpx(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]/red_word[1]*x**2- red_word[2]*x+red_word[3]
    df = diff(f)
    result.append(latex( df ))
    return result 

def p12_diffgpxkh(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**2*(1-red_word[0]*x)
    df = diff(f)
    result.append(latex( df ))
    return result 

def p12_d2f(red_word):#3803017,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x**4- red_word[1]*x**3+ red_word[2]*x
    df = diff(f)
    ddf = diff(df)
    result.append(latex( df ))
    result.append(latex( ddf ))
    return result 

def p12_va(red_word):#3802261,2
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    f = t**3-red_word[0]*t
    df = diff(f)
    ddf = diff(df)
    result.append(latex( df ))
    result.append(latex( ddf ))
    result.append(str( ddf.subs(t,red_word[1]) ))
    tt = solve(df)
    result.append(str( ddf.subs(t,tt[1]) ))
    return result 

def p12_horizontal(red_word):#3802644,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x**3+red_word[1]*x**2- red_word[2]*x+red_word[3]
    df = diff(f)
    xx = solve(df)

    result.append(str( xx[0] ))
    result.append(str( f.subs(x,xx[0]) ))
    result.append(str( xx[1] ))
    result.append(str( f.subs(x,xx[1]) ))
    return result 

if __name__ == '__main__':
    red_word = [8];
    for i in p12_diffgpxkh(red_word):
        print(i)