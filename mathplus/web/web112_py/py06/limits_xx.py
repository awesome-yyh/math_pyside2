# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p06_limit_t4(red_word):#3801556,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (x**4- red_word[1])/(2*x**2-3*x+red_word[2])
    # f = (x**4-8)/(2*x**2-3*x+5)
    result.append(str( limit(f,x, red_word[0]) ))
    # result.append(str( limit(f,x, -2) ))
    return result

def p06_limit_x2(red_word):#3801516,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (x**2- red_word[1]*x+red_word[2])/(x- red_word[3])
    result.append(str( limit(f,x, red_word[0]) ))
    return result

def p06_limit_t2(red_word):#3801973,3
    red_word = list(map(int,red_word))
    result = []
    f = 'Limit[(x^2 - s0)/(2*x^2 + s1*x + s2), x -> ?]'
    result.append( f.replace('s0',str(red_word[0])).replace('s1',str(red_word[1])).replace('s2',str(red_word[2])))
    return result

def p06_limit_h2(red_word):#3801497,1
    result = []
    f = 'Limit[((? + h)^2 - 16)/h, h -> 0]'
    result.append( f.replace('s0',str(red_word[0])))
    return result

def p06_limit_sqrt(red_word):#3803229,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (sqrt(red_word[0]+x)-red_word[1])/x
    result.append(str( limit(f,x, 0) ))
    return result

def p06_limit_dd(red_word):#3802375,2
    result = []
    f = 'Limit[(1/s0 + 1/x)/(s1 + x), x -> ?]'
    result.append( f.replace('s0',str(red_word[0])).replace('s1',str(red_word[1])) )
    return result

def p06_limit_h1(red_word):#3802801,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = ( (red_word[0]+x)**(-1)-red_word[1]**(-1) )/x
    result.append(str( limit(f,x, 0) ))
    return result

def p06_limit_dt2(red_word):#3803094,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]/x - red_word[1]/(x**2+x)
    result.append(str( limit(f,x, 0) ))
    return result

def p06_limit_sqrtx2(red_word):#3802637,3
    result = []
    f = 'Limit[(Sqrt[x^2 + s0] - s1)/(x + s2), x -> ?]'
    result.append( f.replace('s0',str(red_word[0])).replace('s1',str(red_word[1])).replace('s2',str(red_word[2])))
    return result

def p06_limit_t42(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = limit((x**4- red_word[1])/(2*x**2-3*x+ red_word[2]),x,red_word[0])
    result.append(str(f) )
    return result

def p06_a_f(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = ( (red_word[0]+x)**(-1)-red_word[1]**(-1) )/x
    result.append(str( red_word[1]+red_word[3]*red_word[6] ))
    result.append(str( red_word[3]**3 ))
    result.append(str( red_word[1]**(1/2) ))
    result.append(str( red_word[1]*red_word[10]/red_word[3] ))
    result.append('DNE')
    result.append('0')
    return result

if __name__ == '__main__':
    red_word = [-2,3,1]
    for i in p06_limit_t42(red_word):
        print(i)
