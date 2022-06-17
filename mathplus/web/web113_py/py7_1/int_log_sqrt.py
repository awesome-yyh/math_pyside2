# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_1_int_e(red_word):
    red_word = list(map(int,red_word))
    result = []
    # 
    s = 'e^x\\cdot \\left(rj+rw0\\cdot x\\right)'
    s = s.replace('rw0',str(red_word[0])).replace('rj',str(red_word[1]-red_word[0]))
    #
    result.append(s)
    return result

def p7_1_area_log(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    y1 = red_word[0]*log(x); y2 = x*log(x);xxx = [1,red_word[0]]
    return p7_1_area_2(y1,y2,xxx,result)

def p7_1_area_2(y1,y2,xxx,result):
    x = symbols('x')
    ##
    if len(xxx) == 3:
        x1 = xxx[0]; x2 = xxx[1]; x3 = xxx[2];
        s = integrate(y1-y2, (x,x1, x2)) + integrate(y2-y1,(x,x2,x3));
    elif len(xxx) == 2:
        x1 = xxx[0]; x2 = xxx[1];
        s = integrate(y1-y2, (x,x1, x2));
    elif len(xxx) == 4:
        x2 = xxx[1]; x3 = xxx[2];
        s = integrate(abs(y1)-y2, (x,x3, x2));
    ##
    result.append(str(latex(s)).replace('log','ln'))
    return result

def p7_1_int_ze(red_word):
    red_word = list(map(int,red_word))
    result = []
    # 
    s = 'rw0\\cdot e^z\\cdot \\left(-6+6\\cdot z-3\\cdot z^2+z^3\\right)'
    s = s.replace('rw0',str(red_word[0]))
    #
    result.append(s)
    return result

def p7_1_int_log_sqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = 'Integrate[Log[x]/Sqrt[x], {x, rw1, rw0}]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    #
    result.append(s)
    return result

def p7_1_int_log(red_word): #1817186,2
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = integrate(log(red_word[0] *x + red_word[1]), x)
    result.append(latex(s).replace('log','ln'))
    return result

def p7_1_int_dexp(red_word): #1816749,1
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = integrate( x/exp(red_word[0]*x), (x, 0, 1) )
    result.append(latex(s))
    return result

def p7_1_int_cos(red_word): #1817546,1
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = 'Integrate[rw0*x^3*Cos[x^2], {x, Sqrt[Pi/2], Sqrt[Pi]}]'
    s = s.replace('rw0',str(red_word[0]))
    #
    result.append(s)
    return result

def p7_1_int_tcos(red_word): #1816409,2
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = 'Integrate[rw0*t*Cos[t], t]'
    s = s.replace('rw0',str(red_word[0]))
    #
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [7,8]
    for i in p7_1_int_e(red_word):
        print(i)
