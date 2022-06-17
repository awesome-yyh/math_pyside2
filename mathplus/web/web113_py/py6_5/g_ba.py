# 返回元素为字符串的list
# 参数是[100,800]的list
import numpy as np
from sympy import *

def p6_5_g_ba(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    result.append(str(red_word[1]))
    down = red_word[1]
    up = red_word[2]
    f = red_word[0]+x**2
    i = integrate(f,x)
    result.append(latex(i))
    result.append(p6_5_average(f,x,down,up)[1])

    return result

def p6_5_average(f,x,down, up):
    result = []
    s = integrate(f,(x,down,up))
    ave = s/(up-down)
    #
    result.append(str(float(ave)))
    result.append(str(ave))
    return result

if __name__ == '__main__':
    red_word = [ 1,-2,2,-2,2,2,4] # 1290484,7
    for i in p6_5_g_ba(red_word):
        print(i)
