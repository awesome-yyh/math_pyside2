# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
import pyperclip

def p6_3_volume_rotate_y_none():
    x = symbols('x')
    # 
    y1 = 3+(x-4)**2; y2 = 7;xx = solve(y1-y2); d = 0;
    # y1 = 22*x**2-11*x**3; y2 = 0; xx = solve(y1-y2); d = 0; xx = [0, max(xx)];
    y1 = x**2/9;y2=0;x0 = 3;  xx = solve(y1-y2);d = 0; xx = [x0, max(xx)];
    print(xx)
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_2_x_t_2d(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = x**2/red_word[0];y2=red_word[2]; 
    x0=red_word[1]; xx = solve(y1-y2);d=0; xx = [x0, max(xx)];
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_3_volume_rotate_y(y1, y2, xx, d):
    result = []
    x = symbols('x')
    # 
    x0 = xx[0]; x1 = xx[1];
    c = 2*pi*(x-d);
    h = y1-y2;
    v = integrate(c * h, (x,x0, x1))
    result.append(latex(abs(v)))
    return result

if __name__ == '__main__':
    red_word=[16,1,0]
    for i in p6_2_x_t_2d(red_word):
        print(i)