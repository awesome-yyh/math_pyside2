# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p10_1_k_sincos(red_word):#1288001,2
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    a = r'(x/rw0)^2+(y/rw1)^2=1'
    #
    result.append(a.replace('rw0',str(red_word[0])).replace('rw1',str(red_word[1])))
    return result

def p10_1_equ_cosh(red_word):#1288001,2
    red_word = list(map(int,red_word))
    result = []
    ##
    a = '\\left(\\frac{x}{rw1}\\right)^2-\\left(\\frac{y}{rw2}\\right)^2=1'
    #
    result.append(a.replace('rw1',str(red_word[0])).replace('rw2',str(red_word[1])))
    result.append('>=')
    result.append(str(red_word[0]))
    return result

def p10_1_equ_t(red_word):#1289426,5
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    x = red_word[0]+t
    a = 'rw2-rw3\\cdot \\left(x-rw1\\right)'
    a = a.replace('rw1',str(red_word[0])).replace('rw2',str(red_word[1])).replace('rw3',str(red_word[2]))
    b1 = x.subs(t,red_word[3])
    b2 = x.subs(t,red_word[4])
    #
    result.append(str(a))
    result.append(str(b1))
    result.append(str(b2))
    return result

def p10_1_para_sqrt(red_word):#1288001,2
    red_word = list(map(int,red_word))
    result = []
    ##
    a = r'rw0-x^2'
    #
    result.append(a.replace('rw0',str(red_word[0])))

    return result

def p10_1_para_t2(red_word):
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    a = r'\left(\frac{rw1-y}{rw2}\right)^2-rw0'
    #
    a = a.replace('rw0',str(red_word[0])).replace('rw1',str(red_word[1])).replace('rw2',str(red_word[2]))
    result.append(a)
    y = red_word[1]-red_word[2]*t
    result.append(str(y.subs(t,red_word[4])))
    result.append(str(y.subs(t,red_word[3])))
    
    return result

def p10_1_a_b(red_word):
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    xt = r'rw0+r2jr0t'
    yt = r'rw1r3jr1t'
    #
    result.append(xt.replace('rw0',str(red_word[0])).replace('r2jr0',str(red_word[2]-red_word[0])))
    result.append(yt.replace('rw1',str(red_word[1])).replace('r3jr1',str(red_word[3]-red_word[1])))

    return result

if __name__ == '__main__':
    red_word = [-4,7,1,-2];
    for i in p10_1_para_t2(red_word):
        print(i)
