# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p16_implicit2(red_word):#3802767,2
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    g = red_word[0]*x**2-y**2- red_word[1]
    dydx = -1*  diff(g,x)  / diff(g, y); 
    y = sqrt(red_word[0]*x**2- red_word[1])
    dy = diff(y)
    result.append(latex( dydx ))
    result.append(latex( dy ))
    return result 

def p16_implicitxy(red_word):#3802313,2
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    g = x**2- red_word[0]*x*y+y**2- red_word[1]
    dydx = -1*  diff(g,x)  / diff(g, y); 
    result.append(latex( dydx ))
    return result 

def p16_xfx(red_word):#3802652,3
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    s = x+2*red_word[2]**3+red_word[0]*red_word[2]**2*x
    dp1 = solve(s)
    result.append(str( dp1[0] ))
    return result 

def p16_tangent_sincos(red_word):#3802789,1
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    g = y*sin(red_word[0]*x)-x*cos(2*y)
    dydx = -1*  diff(g,x)  / diff(g, y); 
    tan = dydx.subs(x,1/2*pi).subs(y,pi/4)*(x-pi/2)+pi/4
    result.append(latex( tan ))
    return result 

def p16_d2xy(red_word):#3803007,2
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    g = x**2+red_word[0]*y**2- red_word[1]
    dydx = -1*  diff(g,x)  / diff(g, y)
    result.append(str( dydx ))
    result.append('zai dui x qiudao ,yp shi dydx')
    return result 

if __name__ == '__main__':
    red_word = [5,5];
    for i in p16_d2xy_atan(red_word):
        print(i)
