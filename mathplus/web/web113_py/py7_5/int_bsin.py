# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_5_int_bsin(red_word):#1816621
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Simplify[Integrate[rw0*(x^2 - b*x)*Sin[rw1*x], x]]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

def p7_5_int_cossin2(red_word): #1816226,2
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = integrate(cos(x)*(red_word[0]+red_word[1]*sin(x)**2))
    result.append(latex(s))
    return result

def p7_5_int_eatan(red_word): #1817341,3
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = integrate(red_word[1]*exp(atan(x))/(1+x**2),(x,- red_word[2],red_word[0]))
    result.append(latex(simplify(s)))
    return result

if __name__ == '__main__':
    red_word = [ 1,3,1]; 
    for i in p7_5_int_eatan(red_word):
        print(i)