# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_work_spring_natural(red_word):
    red_word = list(map(float,red_word))
    result = []
    x, x0, k = symbols('x x0 k')
    # 
    w0 =  red_word[0];
    l00 = red_word[1];
    l01 = red_word[2];
    w1 =  red_word[3];
    l10 = red_word[4];
    l11 = red_word[5];
    ##
    l00 = l00 / 100;
    l01 = l01 / 100;
    l10 = l10 / 100;
    l11 = l11 / 100;
    equ1 = integrate(k*x, (x,l00-x0, l01-x0));
    equ2 = integrate(k*x, (x,l10-x0, l11-x0));
    x0 = solve([equ1 - w0, equ2 - w1],[k,x0])[0][1]*100
    result.append(str(round(x0,2)))
    return result

if __name__ == '__main__':
    red_word = [27,12,18,45,18,24] #1816142,6
    for i in p6_4_work_spring_natural(red_word):
        print(i)
