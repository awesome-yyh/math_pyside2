# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
import pyperclip

def p6_5_average_none(red_word):
    x = symbols('x')
    # 
    f = 2*x-x**2;xx=[0,5]
    # f = sqrt(x); xx = [0,16]
    # f = 4*sin(x)-2*sin(2*x);xx=[0,pi];
    # f = 7*x**2+3*x+3;xx=[15,25];
    # f = (x-5)**2; xx=[1,7]
    # f = 2*x/(1+x**2)**2;xx = [0,2]
    # f = (18-14*x)**(-1);xx = [-1,1]
    # f = 3*sqrt(x);xx=[0,4]
    # f = 10*sec(x/3)**2;xx=[0,3/4*pi]
    # f = (14-12*x)**(-1);xx = [-1,1]
    return p6_5_ave_c(f,x,xx)

def p6_5_ave_t_12(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    f = red_word[0]*x-x**2
    xx = [red_word[1], red_word[2]]
    return p6_5_average(f,x,xx)

def p6_5_ave_z(red_word):
    red_word = list(map(int,red_word))
    result = []
    #
    result.append(str(red_word[5]))
    result.append(str(red_word[5]))
    result.append(str(red_word[5]-red_word[0]))
    return result

def p6_5_ave_t_f1(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    # 
    f = (red_word[0]-red_word[1]*x)**(-1)
    xx = [red_word[2], red_word[3]]
    return p6_5_average(f,x,xx)

def p6_5_ave_t_d2(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    fave = str(red_word[0])+'/5'
    result.append(fave)
    result.append('0.220')
    result.append('1.207')
    return result

def p6_5_ave_s_2(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    # 
    f = red_word[0]*x**2+red_word[1]*x+red_word[2]
    xx = [red_word[3], red_word[4]]
    return p6_5_ave_c(f,x,xx)

def p6_5_ave_t_sqrt(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    # 
    f = red_word[0]*sqrt(x);xx = [red_word[1], red_word[2]]
    return p6_5_ave_c(f,x,xx)

def p6_5_average_exp(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    s = integrate( red_word[0]*x*exp(-x**2) ,(x,red_word[1],red_word[2]))/(red_word[2]-red_word[1])
    result.append(latex(simplify(s)))
    return result

def p6_5_ave_t_sec(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    # 
    if len(red_word)==4:
        f = red_word[0]*sec(x/red_word[1])**2
        xx = [0,red_word[2]/red_word[3]*pi]
        return p6_5_average(f,x,xx)
    else:
        return ['enter 4 number and cal(just red)']

def p6_5_average_sqrt(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    # 
    f = red_word[0]*x**2*sqrt(red_word[1]+x**3)
    xx = [red_word[3], red_word[2]]
    return p6_5_average(f,x,xx)

def p6_5_average_sin(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    # 
    f = red_word[0]+red_word[1]*sin(pi*x/12)
    xx = [0,12]
    return p6_5_average(f,x,xx)

def p6_5_average_density(red_word): # 1816545,3
    red_word = list(map(float,red_word))
    x = symbols('x')
    # 
    f = red_word[1]/sqrt(x+red_word[2])
    xx = [0,red_word[0]]
    return p6_5_average(f,x,xx)

def p6_5_average(f,x,xx):
    result = []
    down = xx[0];up = xx[1]
    s = integrate(f,(x,down,up))
    ave = simplify(s/(up-down))
    #
    result.append('ave=')
    result.append(str(float(ave)))
    result.append(latex(ave).replace('log','ln'))
    return result

def p6_5_ave_c(f,x,xx):
    ave = p6_5_average(f,x,xx)
    xp = solve(f-float(ave[1]));
    result = ave
    for i in range(len(xp)):
        result.append('c='+str(xp[i]))
    return result

if __name__ == '__main__':
    red_word = [2,0,5]
    for i in p6_5_ave_t_12(red_word):
    # for i in p6_5_average_none(red_word):
        print(i)
