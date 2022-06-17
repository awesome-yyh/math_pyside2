# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p21_ln(red_word):#3804512,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = log(x)
    xx = [1,red_word[0]]
    v=solve( (f.subs(x,xx[1]) - f.subs(x,xx[0])) / (xx[1] - xx[0]) - diff(f) )
    result.append('yes, [1,5]')
    result.append(latex( v[0] ).replace('log','ln'))
    return result 

def p21_sqrt(red_word):#3803693,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sqrt(x)
    xx = [0,red_word[0]]
    v=solve( (f.subs(x,xx[1]) - f.subs(x,xx[0])) / (xx[1] - xx[0]) - diff(f) )
    result.append(latex( v[0] ))
    result.append('up up up line up')
    return result 

def p21_f_f(red_word):#3803844,6
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( (red_word[2]- red_word[3])*red_word[0] ))
    result.append(str( (red_word[2]- red_word[3])*red_word[1] ))
    return result

if __name__ == '__main__':
    red_word = [4,5,6,3,6,3];
    for i in p21_f_f(red_word):
        print(i)
