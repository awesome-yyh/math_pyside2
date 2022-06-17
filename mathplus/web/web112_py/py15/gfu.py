# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p15_gfu(red_word):#3802154,2
    red_word = list(map(int,red_word))
    x,u = symbols('x u')
    result = []
    #
    f = sqrt(red_word[0]+red_word[1]*x)
    df = diff(f)
    result.append(latex( red_word[0]+red_word[1]*x ))
    result.append(latex( sqrt(u) ))
    result.append(latex( df ))
    return result 

def p15_d34(red_word):#3803187,2
    red_word = list(map(int,red_word))
    x,u = symbols('x u')
    result = []
    #
    f = (red_word[0]*x**6+red_word[1]*x**3)**4
    df = diff(f)
    result.append(latex( df ))
    return result 

def p15_dt32(red_word):#3802659,3
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    f = (t+red_word[0])**(2/3)*(red_word[1]*t**2- red_word[2])**3
    df = diff(f)
    result.append(latex( df ))
    return result 

def p15_dsqrtd(red_word):#3803102,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sqrt(x/(x+red_word[0]))
    df = diff(f)
    result.append(latex( df ))
    return result 

def p15_tangent_sinsin(red_word):#3802373,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sin(sin(x))
    df = diff(f)
    tan = df.subs(x,red_word[0]*pi)*(x- red_word[0]*pi)
    result.append('y='+latex( tan ))
    return result 

def p15_diffz(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]**(red_word[1]-x**2)
    df = diff(f)
    result.append(latex(df) )
    return result 

if __name__ == '__main__':
    red_word = [5,4];
    for i in p15_diffz(red_word):
        print(i)