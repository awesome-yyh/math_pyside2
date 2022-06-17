# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_3_a_bx(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    # 橙色的面积
    a = red_word[0];
    b = red_word[1];
    #下面的二选一;
    y = a*x*(x-b)**2; x2 = b;
    return p6_3_a_b(y,x2,result)

def p6_3_a_bsin(red_word): #2694102,2
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    # 橙色的面积
    a = red_word[0];
    b = red_word[1];
    #下面的二选一;
    y = a*sin(b*x**2); x2 = b;
    result.append('V:AAA\pi '.replace('AAA',str(2*a)))
    return p6_3_a_b(y,x2,result)

def p6_3_a_b(y,x2,result):
    x = symbols('x')
    ##
    c = 2*pi*x
    h = y
    v = c * h;
    V = integrate(v, (x,0, x2))
    
    result.append(latex(c))
    result.append(latex(h))
    result.append(latex(V))
    return result

if __name__ == '__main__':
    red_word = [3,1];
    for i in p6_3_a_bsin(red_word):
        print(i)