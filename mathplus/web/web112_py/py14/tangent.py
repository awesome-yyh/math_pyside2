# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p14_tangent_line(red_word):#3802550,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*exp(x)*cos(x)
    df = diff(f)
    tan = df.subs(x,0)*(x)+red_word[1]
    result.append(latex( tan ))
    return result 

def p14_ecos(red_word):#3802430,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    df = 's0e^x\\left(\\cos \\left(x\\right)-\\sin \\left(x\\right)\\right)'
    ddf = 's0e^x\\left(\\cos \\left(x\\right)-\\sin \\left(x\\right)-\\sin \\left(x\\right)-\\cos \left(x\\right)\\right)'
    result.append( df.replace('s0',str(red_word[0])) )
    result.append( ddf.replace('s0',str(red_word[0])) )
    return result 

def p14_limit_sind(red_word):#3803269,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sin(red_word[0]*x)/(red_word[1]*x)
    ll = limit(f,x,0)
    result.append(str( ll ))
    return result 

def p14_limit_cosdsin(red_word):#3802920,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (cos(red_word[0]*x)-1)/sin(red_word[1]*x)
    ll = limit(f,x,0)
    result.append(str( ll ))
    return result 

def p14_difffgsc(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f  = red_word[0]
    fp = red_word[1]
    s  = sin(pi/3)
    sp = cos(pi/3)
    c  = cos(pi/3)
    cp = -sin(pi/3) 
    result.append(latex( fp*s+sp*f ))
    result.append(latex( (cp*f-c*fp)/f**2 ))
    return result 

def p14_diffbig(red_word):#3802920,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(latex( diff(sin(x),x,red_word[0]) ))
    return result 

if __name__ == '__main__':
    red_word = [95,95];
    for i in p14_diffbig(red_word):
        print(i)