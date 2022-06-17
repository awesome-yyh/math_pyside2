# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p34_gsubs_2sqrt(red_word):#3804364,8
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append('3*x^2')
    result.append('1/3')
    result.append('2/9*u^(3/2)')
    result.append('2/9*(x^3+24)^(3/2)+C')
    return result 

def p34_bint_cos(red_word):#3803343,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = cos(red_word[0]*x)
    result.append(latex( integrate(f,x) )+'+C')
    return result 

def p34_bint_sinzcos(red_word):#3803949,1
    red_word = list(map(int,red_word))
    s = symbols('s')
    result = []
    #
    f = sin(s)**red_word[0]*cos(s)
    result.append(latex( integrate(f,s) )+'+C')
    return result 

def p34_bint_gd(red_word):#3803582,30
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = 1/(red_word[0]- red_word[1]*x)
    result.append(str( -red_word[1] ))
    result.append('-1/'+str(red_word[1] ))
    result.append('-ln|u|/'+str(red_word[1] ))
    result.append('C-ln|'+str(1/f) +'|/'+str(red_word[1]))
    return result 

def p34_bint_glnz(red_word):#3804276,11
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (log(x))**red_word[0]/x
    result.append('1/x')
    result.append('1')
    result.append('u^'+str(red_word[-1])+'/'+str(red_word[-1]))
    result.append('C+ln(x)^'+str(red_word[-1]) +'/'+str(red_word[-1]))
    return result 

def p34_bint_gesqrt(red_word):#3804311,11
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append('exp(x)')
    result.append('1')
    result.append('2/3*u^(3/2)')
    result.append('C+2/3*(exp(x)+'+str(red_word[0])+')^(3/2)')
    return result 

def p34_bint_sectan(red_word):#3803819,1
    red_word = list(map(int,red_word))
    s = symbols('s')
    result = []
    #
    f = sec(s)**2*tan(s)**red_word[0]
    result.append(latex( simplify(integrate(f,s)) )+'+C')
    return result 

def p34_bint_sindcos(red_word):#3804091,1
    red_word = list(map(int,red_word))
    s = symbols('s')
    result = []
    #
    f = sin(s)/cos(s)**2
    result.append(latex( simplify(integrate(f,(s,0,pi/red_word[0]))) ))
    return result 

def p34_dint_ez(red_word):#3803749,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = exp(1/x**red_word[0])/x**red_word[1]
    result.append(latex( simplify(integrate(f,(x,1,2))) ))
    return result 

def p34_dint_xe(red_word):#3804396,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = 1/(x*sqrt(log(x)))
    result.append(latex( simplify(integrate(f,(x,exp(red_word[1]),exp(red_word[0])))) ))
    return result 

if __name__ == '__main__':
    red_word = [64,49]
    for i in p34_dint_xe(red_word):
        print(i)
