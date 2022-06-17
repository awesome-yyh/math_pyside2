# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_hydrostatic_S(red_word):#1816412,2
    red_word = list(map(int,red_word))
    result = []
    x,t = symbols('x t')
    ##
    ro = red_word[0]; g = 9.8;
    l =  red_word[1];
    # ro = 1000; g = 9.8; 
    #
    h = l/2*3**(1/2);
    w = l/h*x;
    delta = ro * g;
    F = integrate(delta* (h - x) * w, (x,0, h));
    result.append(str(round(float(F),1)))
    return result

def p8_3_z_dam(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    result.append(str(red_word[2]))
    result.append(str(red_word[7])+'-x')
    result.append(str(red_word[7])+'-x_i')
    result.append(str(red_word[7])+'-x_i')
    f = red_word[7]*x-x**2
    s = integrate(f,x)
    result.append(latex(s))
    ss = integrate(f,(x,0,red_word[8]))*9800
    result.append(str(ss))
    return result

def p8_3_hydrostatic_fx(red_word):#1816489,3
    red_word = list(map(int,red_word))
    result = []
    x,t = symbols('x t')
    ##
    y1 = sqrt(red_word[0]*x)
    y2 = red_word[1]
    dep = red_word[2]
    # 
    delta = 42
    w = 2*y1
    F = delta*integrate(w*(dep-x),(x,0,dep))
    result.append(str(round(float(F),1)))
    return result

if __name__ == '__main__':
    red_word = [20,10,10,10,20,10,6,14,4,4,4,14];
    for i in p8_3_z_dam(red_word):
        print(i)
