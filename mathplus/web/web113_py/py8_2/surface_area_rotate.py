# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np


def p8_2_surface_area_xp(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    y = x**(red_word[0])
    dy = diff(y);
    uy = 2*pi*x*sqrt(1+dy**2); #绕x写y，绕y写x
    ux = 2*pi*y*sqrt(1+dy**2); #绕x写y，绕y写x
    result.append(latex(ux))
    result.append(latex(uy))
    return result

def p8_2_surface_s_exp(red_word):
    result = []
    #
    result.append('look steps')
    result.append('2pi*y')
    result.append('y,kan ti')
    result.append('x0 x1')
    result.append('no.3')
    result.append('sec(theta)^3*d*theta')
    result.append('look result')
    return result

def p8_2_surface_area_rotate_exp(red_word):
    red_word = list(map(int,red_word))
    x,xx = symbols('x xx')
    #
    y = exp(-red_word[0]*x); xx = [0,oo];flag = 'x';
    return p8_2_surface_area_rotate(y,x,xx,flag)

def p8_2_surface_s_x2(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    y = red_word[0]*x**2; xx = [red_word[1],red_word[2]];
    dy = diff(y);
    u = 2*pi*x*sqrt(1+dy**2)
    s = integrate(u,(x, xx[0], xx[1]))
    result.append(str(round(float(s),2)))
    return result

def p8_2_group(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    disp = red_word[0]
    dep  = red_word[1]
    a = dep / (disp/2)**2
    result.append(str(a))

    y = a*x**2; x0 = 0; x1 = disp/2;
    dy = diff(y);
    u = 2*pi*x*sqrt(1+dy**2)
    s = integrate(u,(x, int(x0), int(x1)))
    result.append(latex(simplify(s)))
    return result

def p8_2_surface_area_rotate(y,x,xx,flag):
    result = []
    x0 = xx[0]; x1 = xx[1]
    dy = diff(y);
    if flag == 'y':
        u = 2*pi*x*sqrt(1+dy**2); #绕x写y，绕y写x
    elif flag == 'x':
        u = 2*pi*y*sqrt(1+dy**2); #绕x写y，绕y写x
    
    s = integrate(u,(x, x0, x1));
    result.append('Integrate['+str(u).replace('pi','Pi').replace('exp(','Exp[').replace('sqrt(','Sqrt[')+', {x, '+str(x0)+', Infinity}]')
    return result

if __name__ == '__main__':
    red_word = [3,5,6,9];
    for i in p8_2_surface_s_exp(red_word):
        print(i)
