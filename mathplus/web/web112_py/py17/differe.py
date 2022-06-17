# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p17_diff_ln(red_word):#3802359,3
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    f = red_word[0]*x*log(red_word[1]*x)- red_word[2]*x
    dy = diff(f)
    result.append(latex( dy ).replace('log','ln'))
    return result 

def p17_diff_lnsin(red_word):#3802422,1
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    f = log(red_word[0]*sin(x)**2)
    dy = diff(f)
    result.append(latex( simplify(dy) ).replace('log','ln'))
    return result 

def p17_diff_lnd(red_word):#3802455,1
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    f = log(x*exp(x))/log(red_word[0])
    dy = diff(f)
    result.append(latex( simplify(dy) ).replace('log','ln'))
    return result 

def p17_diff_lnln(red_word):#3802505,1
    red_word = list(map(int,red_word))
    s = symbols('s')
    result = []
    #
    f = log(log(red_word[0]*s))
    dy = diff(f)
    result.append(latex( simplify(dy) ).replace('log','ln'))
    return result 

def p17_diff_ln2(red_word):#3802619,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = log(x**2- red_word[0]*x)
    dy = diff(f)
    result.append(latex( simplify(dy) ))
    dom = '\\left(-\\infty ,0\\right),\\left(s0,\\infty \\right)'
    result.append(dom.replace('s0',str(red_word[0])).replace('log','ln'))
    return result 

def p17_tangent_ln(red_word):#3803196,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = log(x**2- red_word[0]*x+1)
    df = diff(f)
    tan = df.subs(x,red_word[1])*(x- red_word[1])
    result.append(latex( tan ).replace('log','ln'))
    return result 

def p17_diff_sqrtz(red_word):#3802354,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (sqrt(x))**(red_word[0]*x)
    dy = diff(f)
    result.append(latex( simplify(dy) ).replace('log','ln'))
    return result 

if __name__ == '__main__':
    red_word = [7];
    for i in p17_diff_sqrtz(red_word):
        print(i)
