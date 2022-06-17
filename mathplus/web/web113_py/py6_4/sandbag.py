# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_sandbag(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    m = red_word[0];
    h = red_word[1];
    ## 计算
    g = 9.8;
    M = m * g;
    w = M * h;
    #
    result.append(str(abs(round(w,2))))
    return result

def p6_4_sandbag2(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    m = red_word[0];
    h = red_word[1];
    ## 计算
    w = m*h
    #
    result.append(str(abs(round(w,2))))
    return result

def p6_4_T(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    a = red_word[0]; #看题
    h = red_word[1]; #看图，高
    ## 计算
    w = (a/2+a)*h/2
    #
    result.append(str(abs(round(w,2))))
    return result

def p6_4_rope_ab(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    l = red_word[0]; #看题
    w = red_word[1]; #看图，高
    ## 计算
    at = integrate(w*x,(x,0,l))
    b2 = l*w/2
    bt = integrate(w*x+b2,(x,0,l/2))
    #
    result.append(str(w)+'\\cdot x_i')
    result.append(str(l))
    result.append(str(w)+'\\cdot x')
    result.append(str(abs(round(float(at),2))))

    result.append(str(w)+'\\cdot x_i+'+str(b2))
    result.append(str(l/2))
    result.append(str(w)+'\\cdot x+'+str(b2))
    result.append(str(abs(round(float(bt),2))))
    return result

def p6_4_qiu2(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    r = red_word[0]; #看题
    h = red_word[1]; #看图，高
    ## 计算
    w = 900*pi*9.8*integrate((r*2*x-x**2)*(r*2+h-x),(x,0,r))
    #
    result.append(str(abs(round(float(w),3))))
    return result

if __name__ == '__main__':
    red_word = [12,6]
    for i in p6_4_qiu2(red_word):
        print(i)
