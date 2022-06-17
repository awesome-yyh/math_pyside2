# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p20_critical3(red_word):#3803795,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**3+red_word[0]*x**2- red_word[1]*x
    v = solve(diff(f))
    result.append(str( v )[1:-1])
    return result 

def p20_gd2(red_word):#3803840,13
    red_word = list(map(int,red_word))
    x,y = symbols('x y')
    result = []
    #
    g = (y- red_word[0])/(y**2- red_word[1]*y+ red_word[2])
    gp = diff(g)
    result.append(latex( simplify(gp) ))
    result.append('DNE')
    v = solve(gp)
    result.append(str( v )[1:-1])
    return result 

def p20_criticale(red_word):#3803479,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**red_word[0]*exp(- red_word[1]*x)
    v = solve(diff(f))
    result.append(str( v )[1:-1])
    return result 

def p20_absm(red_word):#3803364,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    y = red_word[0]+red_word[1]*x-x**2
    xx = [0, 5];
    return p20_max_min(y,xx,x,result)
    
def p20_absd2(red_word):#3803547,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    y = x/(x**2-x+red_word[0])
    xx = [0, red_word[1]];
    return p20_max_min(y,xx,x,result)

def p20_max_min(y,xx,x,result):
    x1 = solve(diff(y));
    xx1 = [x for x in x1 if (x >= xx[0] and x <= xx[1])]
    xxx =list(set(xx1+xx));
    v = []
    for x0 in xxx:
        v.append(y.subs(x,x0))
    vmax = max(v);vmin = min(v);
    result.append(str( vmin ))
    result.append(str( vmax ))
    return result 

if __name__ == '__main__':
    red_word = [9,9];
    for i in p20_absd2(red_word):
        print(i)
