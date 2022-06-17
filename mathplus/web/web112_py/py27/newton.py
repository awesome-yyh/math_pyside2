# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p27_newton(f,x1):
    x = symbols('x')
    df = diff(f)
    return x1 - f.subs(x,x1)/df.subs(x,x1)

def p27_gnewton(red_word):#3804261,15
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**3+red_word[0]*x- red_word[1]
    x1 = red_word[2]
    df = diff(f)
    result.append(str( df ))
    result.append(str( f.subs(x,x1) ))
    x2 = p27_newton(f,x1)
    result.append(str( round(x2,6) ))
    result.append(str( red_word[0] ))
    result.append(str( red_word[0] ))
    x3 = p27_newton(f,x2)
    result.append(str( round(x3,5) ))
    return result 

def p27_newton4(red_word):#3804390,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**4-x- red_word[0]
    x1 = 1
    x2 = p27_newton(f,x1)
    result.append(str( x2 ))
    return result 

def p27_correct(red_word):#3804482,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = 3*x**4-8*x**3+ red_word[0]
    x1 = 2
    result.append(str( f.subs(x,2) ))
    result.append(str( f.subs(x,3) ))
    result.append(str( 0 ))
    print(float(solve(f)[3]))
    result.append(str( round(float(max(solve(f))),7) ))
    return result 

def p27_roote(red_word):#3803676,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = exp(x)- red_word[0]+x**2
    x1 = solve(red_word[0]-x**2)[0]
    
    xx = p27_newton(f,x1)
    result.append(str( round(float(xx),7) ))
    return result 

def p27_gmaximize(red_word):#3803707,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x*cos(x)
    df = diff(f)
    result.append(str( df ))
    ddf = diff(df)
    result.append(str( ddf ))
    x1 = 0.9
    x2 = p27_newton(df,x1)
    result.append(str( round(float(x2),7) ))
    x3 = p27_newton(df,x2)
    result.append(str( round(float(x3),6) ))
    x4 = p27_newton(df,x3)
    result.append(str( round(float(x4),6) ))
    result.append(str( round(float(x4),6) ))
    result.append(str( 0 ))
    result.append(str( round(float(f.subs(x,pi)),6) ))
    result.append(str( round(float(f.subs(x,x4)),6) ))
    result.append(str( round(float(f.subs(x,x4)),6) ))
    return result 

if __name__ == '__main__':
    red_word = [9];
    for i in p27_correct(red_word):
        print(i)
