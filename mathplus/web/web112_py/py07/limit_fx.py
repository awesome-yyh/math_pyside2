# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p07_limit_fx12(red_word):#3802184,5
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    ex = red_word[0]*x- red_word[1]
    result.append(str(float( ex.subs(x,red_word[4]) )))
    return result

def p07_limit_fx4(red_word):#3802802,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str(red_word[0]) )
    return result

def p07_limit_t4cos(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = limit(x**red_word[0]*cos(red_word[1]/x),x,0)
    result.append(str(f))
    return result

def p07_limit_abs(red_word):#3802327,5
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (x**2+x- red_word[0])/(abs(x- red_word[1]))
    result.append(str( limit(f,x, red_word[2]) ))
    result.append(str( -limit(f,x, red_word[2]) ))
    result.append('No')
    result.append('2 duan down up')
    return result

def p07_limit_gx4(red_word):#3803249,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append('1')
    result.append('1')
    result.append(str(red_word[0]))
    result.append('-2')
    result.append(str(2-red_word[1]))
    result.append('DNE')
    result.append('3 duan last up')
    return result

def p07_limit_sfx(red_word):#3802908,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str(red_word[0]))
    return result    

if __name__ == '__main__':
    red_word = [4,6]; 
    for i in p07_limit_t4cos(red_word):
        print(i)