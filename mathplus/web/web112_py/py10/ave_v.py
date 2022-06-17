# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p10_ave_v4b(red_word):#3802554,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**2- red_word[0]*x+ red_word[1]
    result.append(str( (f.subs(x,4)-f.subs(x,3))/1 ))
    result.append(str( (f.subs(x,4)-f.subs(x,3.5))/0.5 ))
    result.append(str( (f.subs(x,5)-f.subs(x,4))/1 ))
    result.append(str( (f.subs(x,4.5)-f.subs(x,4))/0.5 ))
    result.append(str( diff(f).subs(x,4) ))
    return result 

def p10_diff2(red_word):#3802953,3
    red_word = list(map(int,red_word))
    x,a = symbols('x a')
    result = []
    #
    f = red_word[0]*x**2- red_word[1]*x+ red_word[2]
    result.append(latex( diff(f).subs(x,a) ))
    return result 

def p10_vdt2(red_word):#3802340,1
    red_word = list(map(int,red_word))
    x,a = symbols('x a')
    result = []
    #
    f = red_word[0]/x**2
    df = diff(f)
    result.append(latex( df.subs(x,a) ))
    result.append(str( df.subs(x,1) ))
    result.append(str( df.subs(x,2) ))
    result.append(str( df.subs(x,3) ))
    return result 

def p10_solpe_point_fig(red_word):#3802258,10
    red_word = list(map(int,red_word))
    x,a = symbols('x a')
    result = []
    #
    f = red_word[0]+red_word[1]*x**2-2*x**3
    df = diff(f)
    result.append(str(df.subs(x,a) ))
    result.append(str( df.subs(x,red_word[2])*(x- red_word[2])+ red_word[3] ))
    result.append(str( df.subs(x,red_word[4])*(x- red_word[4])+ red_word[5] ))
    result.append(str( 'xie cha' ))
    return result 

def p10_tangent(red_word):#3802527,7
    red_word = list(map(int,red_word))
    x,a = symbols('x a')
    result = []
    #
    result.append(str( red_word[1] ))
    result.append(str( (red_word[1]- red_word[2])/(red_word[0]) ))
    return result 

if __name__ == '__main__':
    red_word = [2,5,3]; 
    for i in p10_diff2(red_word):
        print(i)