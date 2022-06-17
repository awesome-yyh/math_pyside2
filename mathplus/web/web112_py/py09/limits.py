# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p09_limitd(red_word):#3802709,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (red_word[0]*x- red_word[1]) / (2*x+ red_word[2])
    result.append(str( limit(f,x,oo) ))
    return result 

def p09_limitd2(red_word):#3802589,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (x-red_word[0])/(x**2+red_word[1])
    result.append(str( limit(f,x,-oo) ))
    return result 

def p09_limit_sqrt2d(red_word):#3802441,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (sqrt(x)+x**2)/(red_word[0]*x-x**2)
    result.append(str( limit(f,x,oo) ))
    return result 

def p09_limit_sqrt2(red_word):#3802229,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sqrt(x+red_word[0]*x**2) / (red_word[1]*x-1)
    result.append(str( limit(f,x,oo) ))
    return result 

def p09_limit_sqrt2_(red_word):#3802168,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sqrt(red_word[0]*x**2+x) - red_word[1]*x
    result.append(str( limit(f,x,oo) ))
    return result 

def p09_limit_ed(red_word):#3802687,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (red_word[0]-exp(x))/(red_word[1]+red_word[2]*exp(x))
    result.append(str( limit(f,x,oo) ))
    return result 

def p09_limit_xxy(red_word):#4049834,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    d = x**2+x- red_word[2]
    f = (red_word[0]*x**2+x- red_word[1])/d
    xx = solve(d)
    result.append(str( xx[0] ))
    result.append(str( xx[1] ))
    result.append(str( limit(f,x,oo) ))
    return result 

def p09_limit_xxxy(red_word):#3802707,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    d = x**2-x**4
    f = (red_word[0]+x**4)/d
    xx = solve(d)
    result.append(str( xx[0] ))
    result.append(str( xx[1] ))
    result.append(str( xx[2] ))
    result.append(str( limit(f,x,oo) ))
    return result 

if __name__ == '__main__':
    red_word = [5]; 
    for i in p09_limit_xxxy(red_word):
        print(i)