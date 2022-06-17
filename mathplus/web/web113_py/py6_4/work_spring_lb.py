# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_ft(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    l1 = red_word[0];
    w1 = red_word[1]; 
    l2 = red_word[2]/12; #单位ft , 如果是in, /12 化为 ft
    ## 计算
    k = 2*w1/l1**2;
    w2 = 1/2 * k * l2**2
    #
    result.append(str(w2))
    return result

def p6_4_work_spring_lb(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    #
    f0 =      red_word[0]; #0.6/(0.15-0.13); #单位lb
    beyond0 = red_word[1]/12; #单位ft , 如果是in, /12 化为 ft
    beyond1 = red_word[2]/12; #单位ft , 如果是in, /12 化为 ft
    ## 计算
    f = f0 / beyond0 * x;
    w = integrate(f, (x,0, beyond1))
    #
    result.append(str(round(w,3)))
    return result

if __name__ == '__main__':
    red_word = [1,6,3] #1816293,3
    for i in p6_4_ft(red_word):
        print(i)
