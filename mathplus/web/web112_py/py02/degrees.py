# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p02_degrees(red_word):#3806078
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(r'\frac{s0}{180}\cdot \pi'.replace('s0',str(red_word[0])))
    return result

def p02_degrees_sinsec(red_word):#3806075,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    result.append('cosx*cosy-sinx*siny')
    return result

def p02_solvecos(red_word):#3806219,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    if red_word[0]/red_word[1] == 2:
        result.append(r'\frac{\pi }{3},\frac{5\pi }{3}')
    else:
        result.append('nocode')
    return result

def p02_solvesin2(red_word):#3805921,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    if red_word[0]/red_word[1] == 2:
        result.append(r'\frac{\pi }{4},\frac{3\pi }{4},\frac{5\pi }{4},\frac{7\pi }{4}')
    else:
        result.append('nocode')
    return result

def p02_solvesin(red_word):#3806478,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    if red_word[0] == red_word[1]:
        result.append(r'\left[0,\frac{\pi }{6}\right],\left[\frac{5\pi }{6},2\pi \right]')
    else:
        result.append('nocode')
    return result


if __name__ == '__main__':
    red_word = [3,3]; 
    for i in p02_solvesin(red_word):
        print(i)