# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_5_ave_b(red_word): # 1816414,4
    red_word = list(map(float,red_word))
    x, b = symbols('x b')
    # 
    f = red_word[0]+red_word[1]*x-red_word[2]*x**2
    xx = [0, b]
    avee = red_word[3];
    return p6_5_average(f,x,xx,avee)

def p6_5_average(f,x,xx,avee):
    result = []
    down = xx[0];up = xx[1]
    s = integrate(f,(x,down,up))
    ave = s/(up-down)
    #
    result.append('Solve[' + str(ave).replace('**','^') + '==' + str(avee) + ']')
    return result

if __name__ == '__main__':
    red_word = [3,10,6,4]
    for i in p6_5_ave_b(red_word):
        print(i)
