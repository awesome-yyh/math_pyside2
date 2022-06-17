# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
# 1OC 2CB 3AB 4OA
def p6_2_figureR1_0C(red_word):
    return p6_2_figure(red_word,R = 1,D = 1)
def p6_2_figureR1_CB(red_word):
    return p6_2_figure(red_word,R = 1,D = 2)
def p6_2_figureR1_AB(red_word): #4101020
    return p6_2_figure(red_word,R = 1,D = 3)
def p6_2_figureR1_OA(red_word):
    return p6_2_figure(red_word,R = 1,D = 4)

def p6_2_figureR2_0C(red_word):
    return p6_2_figure(red_word,R = 2,D = 1)
def p6_2_figureR2_CB(red_word):
    return p6_2_figure(red_word,R = 2,D = 2)
def p6_2_figureR2_AB(red_word): #1816521,2
    return p6_2_figure(red_word,R = 2,D = 3)
def p6_2_figureR2_OA(red_word):
    return p6_2_figure(red_word,R = 2,D = 4)

def p6_2_figureR3_0C(red_word):
    return p6_2_figure(red_word,R = 3,D = 1)
def p6_2_figureR3_CB(red_word):
    return p6_2_figure(red_word,R = 3,D = 2)
# def p6_2_figureR3_AB(red_word): #1816477
#     return p6_2_figure(red_word,R = 3,D = 3)
def p6_2_figureR3_OA(red_word):
    return p6_2_figure(red_word,R = 3,D = 4)

def p6_2_figureR4_0C(red_word):
    return p6_2_figure(red_word,R = 4,D = 1)
def p6_2_figureR4_CB(red_word):
    return p6_2_figure(red_word,R = 4,D = 2)
def p6_2_figureR4_AB(red_word):
    return p6_2_figure(red_word,R = 4,D = 3)
def p6_2_figureR4_OA(red_word):
    return p6_2_figure(red_word,R = 4,D = 4)

def p6_2_figure(red_word,R,D):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    ##组装
    a = red_word[0]
    b = red_word[1]
    if R == 1:
        y1 = a*x**b; y2 = 0;
    elif R == 2:
        y1 = a*sqrt(x); y2 = a;
    else:
        y1 = a*x**b; y2 = a*sqrt(x);
    
    if D == 1:
        d = 0;
        ia = 2*pi*(x-d)*(y1-y2);
    elif D == 2:
        d = a;
        ia = pi * ((y1-d)**2 - (y2-d)**2);
    elif D == 3:
        d = 1;
        ia = 2*pi*(x-d)*(y1-y2);
    else:
        d = 0;
        ia = pi * ((y1-d)**2 - (y2-d)**2);
    
    ##
    s = integrate(ia, (x,0, 1));
    ##
    result.append(str(abs(s)))
    result.append(latex(abs(s)))
    return result

if __name__ == '__main__':
    red_word = [3,5];
    for i in p6_2_figureR3_AB(red_word):
        print(i)

