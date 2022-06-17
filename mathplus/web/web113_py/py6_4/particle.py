# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_particle(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    y = red_word[0]/(red_word[1]+x)**2;
    l = red_word[2];
    ## 计算
    w = integrate(y,(x,0,l))
    #
    result.append(str(abs(round(w,2))))
    return result

if __name__ == '__main__':
    red_word = [6,1,5] # 1816461,3
    for i in p6_4_particle(red_word):
        print(i)
