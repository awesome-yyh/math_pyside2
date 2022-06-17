# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_1_length_arc_x(red_word): #1816649,4
    red_word = list(map(int,red_word))
    result = []
    #
    s = sqrt(1+red_word[0]**2)
    ##
    result.append(latex(s*(red_word[2]+red_word[3])))

    return result

def p8_1_s_len_kh(red_word):#1816436,2
    red_word = list(map(int,red_word))
    x,t = symbols('x t')
    result = []
    #
    y =  sqrt(red_word[0]*(x+red_word[1])**3); 
    x0 = 0; x1 = red_word[2]
    dy = diff(y);
    dyy = 1 + dy**2;
    dyy = dyy.subs(x, t);
    u = sqrt(dyy)
    ##
    s = integrate(u, (t,x0, x1));
    #
    result.append(latex(simplify(s)))

    return result

def p8_1_length_arc_xpower(red_word):#1816436,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = red_word[0]+red_word[1]*x**(3/2); xx = [0, 1];
    return p8_1_length_arc(y,xx)

def p8_1_length_arc_xcosh(red_word):#1816283,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    s = r'\frac{\sinh \left(2c3\right)}{rw1}'
    s = s.replace('2c3',str(red_word[2]*red_word[3])).replace('rw1',str(red_word[1]))
    result.append(s)

    return result

def p8_1_length_arc(y,xx):
    result = []
    x,t = symbols('x t')
    ##
    x0 = xx[0];x1 = xx[1];
    dy = diff(y);
    dyy = 1 + dy**2;

    dyy = dyy.subs(x, t);
    u = sqrt(dyy)
    ##
    result.append('integral factor: ')
    result.append(str(simplify(u)))
    # s = integrate(u, (t,x0, x1));
    # #
    # result.append(latex(s))
    # result.append(str(round(float(s),3)))
    return result

def p8_1_s_len(red_word):
    red_word = list(map(int,red_word))
    x,t = symbols('x t')
    result = []
    ##
    y = red_word[0]*x**2
    x0 = red_word[1];x1 = red_word[2];
    dy = diff(y);
    dyy = 1 + dy**2;
    dyy = dyy.subs(x, t);
    u = sqrt(dyy)
    ##
    s = integrate(u, (t,x0, x1));
    #
    result.append(str(round(float(s),2)))
    return result

if __name__ == '__main__':
    red_word = [4,5,1];
    for i in p8_1_s_len_kh(red_word):
        print(i)

