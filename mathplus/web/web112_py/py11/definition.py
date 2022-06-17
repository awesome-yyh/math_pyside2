# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p11_definition(red_word):#3803115,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    gp = '-\\frac{1}{2}\\left(s0-x\\right)^{-\\left(\\frac{1}{2}\\right)}'
    df = '\\left(-\\infty ,s0\\right]'
    dd = '\\left(-\\infty ,s0\\right)'
    result.append( gp.replace('s0',str(red_word[0])) )
    result.append( df.replace('s0',str(red_word[0])) )
    result.append( dd.replace('s0',str(red_word[0])) )
    return result 

def p11_diff12(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    y = red_word[0]*x**2+red_word[1]*x+red_word[2]
    result.append( latex(diff(y,x)) )
    result.append( latex(diff(diff(y,x)),x) )
    result.append( 'are' )
    result.append( 'a linear' )
    result.append( 'constant' )
    return result 

def p11_table(red_word):#3802756,6
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( round((red_word[1]- red_word[0])/7 ,3) ))
    result.append(str( round((red_word[2]- red_word[0])/14 ,3) ))
    result.append(str( round((red_word[3]- red_word[1])/14 ,3) ))
    result.append(str( round((red_word[4]- red_word[2])/14 ,3) ))
    result.append(str( round((red_word[5]- red_word[3])/14 ,3) ))
    result.append(str( round((red_word[5]- red_word[4])/7 ,3) ))
    result.append('down ~~ up')
    return result 

if __name__ == '__main__':
    red_word = [4,5,2];
    for i in p11_diff12(red_word):
        print(i)