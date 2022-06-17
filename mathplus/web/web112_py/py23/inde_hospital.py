# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p23_limit2d(red_word):#3803963,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (x**2- red_word[1]*x- red_word[2])/(x- red_word[3])
    result.append(str( limit(f,x,red_word[0]) ))
    return result 

def p23_limitsind(red_word):#3804132,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (1-sin(x))/(1+cos(red_word[0]*x))
    result.append(str( limit(f,x,pi/2) ))
    return result 

def p23_glnd_sqrt(red_word):#3803863,18
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    up = log(red_word[0]*x)
    down = sqrt(red_word[1]*x)
    f = up/down
    #
    result.append('oo')
    result.append('oo')
    result.append('1/x')
    result.append(latex(diff(down)))
    result.append(latex(down))
    result.append('0')
    result.append('0')
    return result 

def p23_edsin(red_word):#3804474,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (exp(red_word[0]*x)-exp(- red_word[1]*x)- red_word[2]*x)/(x-sin(x))
    #
    result.append(latex(limit(f,x,0)))
    return result 

def p23_xsin(red_word):#3803997,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x*sin(red_word[0]*pi/x)
    #
    result.append(latex(limit(f,x,oo)))
    return result 

def p23_cotsin(red_word):#3803945,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = cot(red_word[0]*x)*sin(red_word[1]*x)
    #
    result.append(latex(limit(f,x,0)))
    return result 

def p23_ddln(red_word):#3803548,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x/(x-1) - red_word[1]/log(x)
    #
    result.append(latex(limit(f,x,1)))
    return result 

if __name__ == '__main__':
    red_word = [1,1,2];
    for i in p23_edsin(red_word):
        print(i)
