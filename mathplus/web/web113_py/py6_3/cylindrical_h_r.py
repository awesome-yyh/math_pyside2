# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_3_cylindrical_h_r(red_word):
    red_word = list(map(int,red_word))
    result = []
    h,r = symbols('h r')
    # 
    H = red_word[0]*h;
    R = red_word[1]*r;

    s = pi*R**2 * H / 3;
    result.append(latex(abs(s)))
    return result

def p6_3_t_cylindrical(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    s1 = '\\frac{y^2}{rw0}'
    s1 = s1.replace('rw0',str(red_word[0]))
    
    s2 = 'rw1-\\frac{1}{rw0}\\cdot y^2'
    s2 = s2.replace('rw0',str(red_word[0])).replace('rw1',str(red_word[1]))

    s3 = '\\frac{rw1}{2}\\cdot y^2-\\frac{1}{4rw0}\\cdot y^4'
    s3 = s3.replace('rw1',str(red_word[1])).replace('4rw0',str(4*red_word[0]))

    # y = 2*pi*x*(red_word[1]-1/red_word[0]*x**2)
    # print(y)
    # s4 = integrate(y,(x,0,red_word[1]))

    #
    result.append(s1)
    result.append(s2)
    result.append(s3)
    result.append('mathematica')
    return result

if __name__ == '__main__':
    red_word = [7,63,7];# 1816112,2
    for i in p6_3_t_cylindrical(red_word):
        print(i)
