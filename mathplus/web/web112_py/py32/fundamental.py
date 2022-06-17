# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p32_dint3(red_word):#3803936,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = 4/red_word[1]*x**3-3/ red_word[2]*x**2+2/red_word[3]*x
    result.append(str( integrate(f,(x,0,red_word[0])) ))
    return result 

def p32_dintkk(red_word):#3803896,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (x+red_word[0])*(x- red_word[1])
    result.append(str( integrate(f,(x,0,1)) ))
    return result 

def p32_dinte(red_word):#3804183,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x**exp(1)+red_word[1]*exp(x)
    result.append(latex( integrate(f,(x,0,1)) ))
    return result 

def p32_dintdx2(red_word):#3803452,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]/(1+x**2)
    result.append(latex( integrate(f,(x,1/sqrt(3),sqrt(3))) ))
    return result 

def p32_dintsqrt(red_word):#3804310,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sqrt(x)
    result.append('y-'+str(sqrt(red_word[0])))
    result.append(latex( integrate(f,(x,0,red_word[0])) ))
    return result 

if __name__ == '__main__':
    red_word = [4]
    for i in p32_dintsqrt(red_word):
        print(i)
