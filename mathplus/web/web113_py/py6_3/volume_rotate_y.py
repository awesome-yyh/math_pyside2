# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
import pyperclip

def p6_3_volume_rotate_y_none(red_word):
    x = symbols('x')
    # 
    # y1 = 12*sqrt(x); y2 = 0;xx = solve(y1-y2); d = -3;xx=[0, 1]
    # y1 = 1+x**2; y2=0;xx=[1,2];d=0;
    y1 = 10+(x-4)**2; y2 = 11;xx = solve(y1-y2); d = 0;
    # y1 = 22*x**2-11*x**3; y2 = 0; xx = solve(y1-y2); d = 0; xx = [0, max(xx)];
    # y1 = 3/x;y2=0;xx=[1,2];d=0
    # y1 = 5-x;y2=14-(x-3)**2;xx = solve(y1-y2); d = 0;
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_3_v_t_kh(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    # 
    y1 = red_word[0]+(x- red_word[1])**2;y2=red_word[2]
    xx = solve(y1-y2); d = 0;
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_3_v_t_j(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    # 
    y1 = red_word[0]-x; y2 = red_word[1]-(x- red_word[2])**2; 
    xx = solve(y1-y2); d = 0;
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_3_v_t_d(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    # 
    y1 = red_word[0]/x; y2 = 0; xx = [red_word[2], red_word[3]]; d = 0;
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_3_v_t_e2(red_word):
    red_word = list(map(int,red_word))
    result = []
    ##
    s1 = 'rw0\\cdot \\pi \\cdot \\left(1-e^{-1}\\right)'
    s1 = s1.replace('rw0',str(red_word[0]))
    result.append(s1)
    #
    return result

def p6_3_v_t_sqrt01(red_word):
    red_word = list(map(int,red_word))
    result = []
    ##
    s1 = '\\frac{4rw0}{5}\\cdot \\pi '
    s1 = s1.replace('4rw0',str(int(4*red_word[0])))
    result.append(s1)
    return result

def p6_3_v_t_sqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    ##
    s1 = 52*red_word[0]
    s2 = '\\frac{s1\\cdot \\pi }{15}'
    s2 = s2.replace('s1',str(int(s1)))
    result.append(s2)
    return result

def p6_3_v_napkin(red_word):
    red_word = list(map(int,red_word))
    result = []
    ##
    s1 = 'the amount of...'
    s2 = r'd73\cdot \pi \cdot h^3'
    # s2 = r'd73\\cdot \\pi \\cdot h^3'
    s2 = s2.replace('d73',str((red_word[0]**3/6)))
    result.append(s1)
    result.append(s2)
    return result

def p6_3_volume_rotate_y_222(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    # 
    y1 = 2-x**2; y2 = x**2; xx = solve(y1-y2); d = red_word[0];
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_3_volume_rotate_y_x4(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    # 
    y1 = x**4; y2 = 0; xx = [0, 2]; d = red_word[0];
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_3_volume_rotate_y_x2(red_word):#1817151,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    # 
    y1 = red_word[0] + x**2; y2 = 0; xx = [red_word[1], red_word[2]]; d = 0;
    return p6_3_volume_rotate_y(y1, y2, xx, d)

def p6_3_int3(red_word):#1576461,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    y = (red_word[0]*x - red_word[1] * x**2)*x
    inty = integrate(y,x)
    dinty = integrate(y,(x,0,1))*2*pi
    result.append(latex( inty ))
    result.append(latex( dinty ))
    return result

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
    red_word = [20,0,1];
    for i in p6_3_v_t_sqrt01(red_word):
        print(i)
