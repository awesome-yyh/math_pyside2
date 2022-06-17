# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p03_zdsqrt(red_word):#3798732,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( red_word[1]**8/red_word[0]**3 ))
    result.append( r'x^{-\left(\frac{s2}{3}\right)}'.replace('s2',str(red_word[2])) )
    return result

def p03_cbx(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    b = (red_word[3]/red_word[1])**(1/(red_word[2]-red_word[0]))
    a = red_word[1]/b**(red_word[0])
    f = int(a)*int(b)**x
    result.append(latex(f))
    return result

def p03_by3(red_word):#3798913,2
    red_word = list(map(int,red_word))
    b, y = symbols('b y')
    result = []
    #
    result.append(latex( b**8*(2*b)**red_word[0] ))
    result.append(latex( (6*y**3)**4/(2*y**red_word[1]) ))
    return result

def p03_e4(red_word):#3798369,2
    red_word = list(map(int,red_word))
    b, y = symbols('b y')
    result = []
    #
    result.append(r'e^x-s0'.replace('s0',str(red_word[0])))
    result.append(r'e^{x-s1}'.replace('s1',str(red_word[1])))
    result.append(r'-e^x')
    result.append(r'e^{-x}')
    result.append(r'-e^{-x}')
    return result

def p03_gdoubling(red_word):#3799425
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    result.append(str(red_word[1]*2))
    result.append(str(red_word[1]*2))
    result.append(str(red_word[0] * 2**(red_word[1]*2)))
    result.append(r'2t')
    result.append(r'2t')
    result.append(latex(red_word[0]*4**t))
    result.append(r'2')
    result.append(r'4')
    result.append(r'4/3')
    result.append(str(round(red_word[0]*2**(4/3))))
    result.append(r'up large')
    result.append(r'2.8 look picture')
    result.append(r'2.8 look picture')
    return result

if __name__ == '__main__':
    red_word = [1,20,3,320]; 
    for i in p03_cbx(red_word):
        print(i)