# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p02_trigonometric_sin(red_word):#3806319,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    theta = asin(red_word[0]/red_word[1])

    result.append(latex(cos(theta)))
    result.append(latex(tan(theta)))
    result.append(latex(cot(theta)))
    result.append(latex(sec(theta)))
    result.append(latex(csc(theta)))
    return result

def p02_trigonometric_cos(red_word):#3806092,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    theta = acos(-1/red_word[0])

    result.append(latex(sin(theta)))
    result.append(latex(tan(theta)))
    result.append(latex(cot(theta)))
    result.append(latex(sec(theta)))
    result.append(latex(csc(theta)))
    return result


if __name__ == '__main__':
    red_word = [8]; 
    for i in p02_trigonometric_sin(red_word):
        print(i)