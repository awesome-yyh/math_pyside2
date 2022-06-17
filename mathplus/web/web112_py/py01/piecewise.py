# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_piecewise1(red_word):#3799103,6
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    f1 = x+red_word[2]
    f2 = red_word[3]-x
    #
    return p01_piecewise(f1, f2, x, result,red_word)

def p01_piecewise(f1,f2,x,result,red_word):
    result.append(str(f1.subs(x,-red_word[0])))
    result.append(str(f2.subs(x,0)))
    result.append(str(f2.subs(x,red_word[1])))
    result.append('up kong shi down')
    return result

if __name__ == '__main__':
    red_word = [6,3,5,2,6,3];
    for i in p01_piecewise1(red_word):
        print(i)