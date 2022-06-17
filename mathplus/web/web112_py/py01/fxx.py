# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_fxx2(red_word):#3799075,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    f = red_word[0]*x**2 - x + red_word[1]
    #
    return p01_fxx(f,x,result, red_word[2])

def p01_fxx(y,x,result,rw2):
    a,h = symbols('a h')
    result.append(str(float(y.subs(x,rw2))))
    result.append(str(float(y.subs(x,-rw2))))
    result.append(latex(y.subs(x,a)))
    result.append(latex(y.subs(x,-a)))
    result.append(latex(y.subs(x,a+1)))
    result.append(latex(2*y.subs(x,a)))
    result.append(latex(y.subs(x,2*a)))
    result.append(latex(y.subs(x,a**2)))
    result.append(latex((y.subs(x,a))**2))
    result.append(latex(y.subs(x,a+h)))
    return result

if __name__ == '__main__':
    red_word = [ 2,3,2];
    for i in p01_fxx2(red_word):
        print(i)