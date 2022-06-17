# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_hydrostatic_J_ft(red_word):
    red_word = list(map(float,red_word))
    result = []
    x= symbols('x')
    #矩形，从下往上建立坐标
    h = red_word[0];
    w = red_word[1];
    d = red_word[2]; #上底边，下底边, 高, 到顶部距离
    delta = 62.5; #ft专用
    ## 计算 side
    F = integrate(delta * x * w, (x,d, d+h));
    #
    result.append(str(round(float(F))))
    return result

if __name__ == '__main__':
    red_word = [3,7,2] #806449,3
    for i in p8_3_hydrostatic_J_ft(red_word):
        print(i)
