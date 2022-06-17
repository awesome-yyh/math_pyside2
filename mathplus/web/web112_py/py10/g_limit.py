# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p10_g_limit(red_word):#3802196,28
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = sqrt(x)
    result.append(latex( f ))
    result.append(latex( red_word[0] ))
    result.append(latex( f ))
    result.append(latex( f ))
    result.append(latex( f+ red_word[1] ))
    mtan = limit(1/(f+ red_word[1]),x,red_word[0])
    result.append(str( mtan ))
    result.append(latex( mtan*(x- red_word[0])+ red_word[1] ))
    return result 

def p10_g_limitd(red_word):#3803070,52
    red_word = list(map(int,red_word))
    x,a = symbols('x a')
    result = []
    #
    f = sqrt(x)
    result.append( 'a+'+str( red_word[2] ))
    result.append(str( red_word[27]- red_word[30] ))
    result.append(str( red_word[31]- red_word[26] ))
    result.append(str( red_word[43] ))
    result.append(str( red_word[43]/ (a+ red_word[-1])**2))
    return result

def p10_g_ball(red_word):#3802933,33
    red_word = list(map(int,red_word))
    x,a = symbols('x a')
    result = []
    #
    f = sqrt(x)
    result.append( str( red_word[2] ))
    result.append( str( red_word[2] ))
    t1last = red_word[0]*red_word[2]-16*red_word[2]**2
    result.append( str( t1last ))
    t21 = solve(x+16*t1last/x-red_word[0])[0]
    result.append( str( t21 ))
    result.append( str( t1last/t21 ))
    result.append( str( red_word[2] ))
    result.append( str( red_word[2]*(-16)+t21 ))
    return result

if __name__ == '__main__':
    red_word = [49,49,2,49,2,2,2,2,2,2,49,49,2,2,2,49,2,2,2,49,34,2,2,2]
    for i in p10_g_ball(red_word):
        print(i)