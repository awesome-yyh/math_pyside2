# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_4_volume_xy(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    y1 = red_word[0]/(x**2+red_word[1]*x+red_word[2])
    x0 = 0; x1 = 1;
    ##x
    a = pi * y1**2;
    vx = integrate(a,(x,0,1))
    result.append(latex(abs(simplify(vx))).replace('log','ln'))
    ##y
    c = 2*pi*x
    h = y1;
    v = integrate(c * h, (x,x0, x1))
    result.append(latex(abs(simplify(v))).replace('log','ln'))
    return result

if __name__ == '__main__':
    red_word = [10,5,6];
    for i in p7_4_volume_xy(red_word):
        print(i)
        