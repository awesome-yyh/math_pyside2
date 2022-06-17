# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_5_int_nx(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = r'rw0\cdot e^rw1\cdot x'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

def p7_5_int_t_1d2(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    f = (x- red_word[1])/(x**2- red_word[2]*x- red_word[3])
    #
    w = integrate(f,(x,red_word[4],red_word[0]))
    result.append(latex(simplify(w)).replace('log','ln'))
    return result

def p7_5_int_redxe(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    a = red_word[0]
    b = red_word[2]
    #
    result.append('\\frac{'+str(a)+'}{'+str(b)+'}\\cdot e^{-x^'+str(b)+'}\\cdot \\left(-1-x^'+str(b)+'\\right)')
    return result

def p7_5_int_redsqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    a = red_word[0]
    b = red_word[1]
    c = red_word[2]
    #
    w = integrate(c*x**2/sqrt(1-x**2),(x,0,sqrt(a)/a))
    result.append(latex(w))
    return result

def p7_5_int_atan(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = r'rw0\cdot \left(-\sqrt{x}+\left(1+x\right)\cdot \operatorname{atan}\left(\sqrt{x}\right)\right)'
    s = s.replace('rw0',str(red_word[0]))
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [8,1,5,6,0]; #1816197
    for i in p7_5_int_atan(red_word):
        print(i)