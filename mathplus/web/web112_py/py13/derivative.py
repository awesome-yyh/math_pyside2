# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p13_derivative2(red_word):#3802133,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (1+red_word[0]*x**2)*(x-x**2)
    df = diff(f)
    result.append(latex( df ))
    result.append(latex( df ))
    result.append('yes')
    return result 

def p13_diff_exp(red_word):#3802576,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (red_word[0]*x**2- red_word[1]*x)*exp(x)
    df = diff(f)
    result.append(latex( df ))
    return result 

def p13_diff_dexp(red_word):#3803073,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x/exp(x)
    df = diff(f)
    result.append(latex( df ))
    return result 

def p13_sqrtd(red_word):#3802910,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sqrt(x)/(red_word[0]+x)
    df = diff(f)
    result.append(latex( df ))
    return result 

def p13_d2d(red_word):#3802304,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**(red_word[0])/(red_word[1]+x)
    df = diff(f)
    ddf = diff(df)
    result.append(str( ddf.subs(x,red_word[2]) ))
    return result 

def p13_fg(red_word):#3802691,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**(red_word[0])/(red_word[1]+x)
    df = diff(f)
    ddf = diff(df)
    result.append(str( ddf.subs(x,2) ))
    return result 

def p13_difffg(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f  = red_word[0]
    fp = red_word[1]
    g  = red_word[2]
    gp = red_word[3]
    result.append(str( fp*g+f*gp ))
    result.append(str( (fp*g-f*gp)/g**2 ))
    result.append(str( -(fp*g-f*gp)/f**2 ))
    return result 

if __name__ == '__main__':
    red_word = [1,7,-2,5];
    for i in p13_difffg(red_word):
        print(i)