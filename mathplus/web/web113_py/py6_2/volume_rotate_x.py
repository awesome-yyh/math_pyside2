# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
import pyperclip

def p6_2_volume_rotate_x_none():
    x = symbols('x')
    # 
    # y1 = 4*x; y2 = 4*sqrt(x); xx = solve(y1-y2); d = 4;
    # y1 = 1+sec(5*x); y2 = 3;xx=[-pi/15,pi/15];d=1;
    y1 = x**2/4; y2=1/2*x; xx = solve(y1-y2); d = 0;
    # y1 = 2*sqrt(x); y2 = 0; xx = solve(y1-y2); d = 0;print(xx);xx=[2,xx[0]]
    # y1 = 2*sqrt(25-x**2); y2 = 0; xx = [1, 3]; d = 0;
    # y1 = 2/x; y2 = 0; xx = [1, 5]; d = -1;
    return p6_2_volume_rotate_x(y1,y2,xx,d)

def p6_2_t_fan_2(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    y1 = red_word[1]/red_word[0]*x**2; y2 = red_word[2]/red_word[3]*x;
    xx = solve(y1-y2); d = 0;
    return p6_2_volume_rotate_x(y1,y2,xx,d)

def p6_2_x_t_d(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    y1 = red_word[1]/x; y2 = red_word[2]; xx = [red_word[3], red_word[4]]; d = red_word[0];
    return p6_2_volume_rotate_x(y1,y2,xx,d)

def p6_2_volume_rotate_x_4sqrt(red_word):
    x = symbols('x')
    # 
    y1 = 4*x; y2 = 4*sqrt(x); xx = solve(y1-y2); d = red_word[0];
    return p6_2_volume_rotate_x(y1,y2,xx,d)

def p6_2_volume_rotate_x(y1,y2,xx,d):
    result = []
    x = symbols('x')
    # 
    x0 = xx[0]; x1 = xx[1];
    a = pi * ((y1-d)**2 - (y2-d)**2);
    s = integrate(a, (x,x0, x1))
    ls = latex(abs(s)).replace('log','ln')
    result.append(ls)
    return result

if __name__ == '__main__':
    red_word = [4,1,1,2] #1291778,1
    for i in p6_2_t_fan_2(red_word):
    # for i in p6_2_volume_rotate_x_none():
        print(i)
