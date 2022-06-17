# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p33_bint_sqrtd(red_word):#3803494,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (red_word[0]+sqrt(x)+x)/x
    result.append(latex( integrate(f,x) )+'+C')
    return result 

def p33_bint_2d2(red_word):#3803395,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x**2+red_word[1]+red_word[2]/(x**2+1)
    result.append(latex( integrate(f,x) )+'+C')
    return result 

def p33_bint_sectan(red_word):#3803692,2
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    f = sec(t)*(red_word[0]*sec(t)+red_word[1]*tan(t))
    result.append(latex( integrate(f,t) )+'+C')
    return result 

def p33_dint_kk2(red_word):#3803520,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (red_word[0]*x- red_word[1])*(red_word[2]*x**2+red_word[3])
    result.append(latex( integrate(f,(x,0,2)) ))
    return result 

def p33_dint_d2d3(red_word):#3804257,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = 1/x**2- red_word[1]/x**3
    result.append(latex( integrate(f,(x,1,red_word[0])) ))
    return result 

def p33_dint_mz(red_word):#3804163,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**red_word[0]+red_word[1]**x
    result.append(latex( integrate(f,(x,0,1)) ))
    return result 

def p33_dint_particle(red_word):#3803817,3
    red_word = list(map(float,red_word))
    t = symbols('t')
    result = []
    #
    v = red_word[0]*t- red_word[1]
    result.append(latex( integrate(v,(t,0,red_word[2])) ))
    v0 = solve(red_word[0]*t- red_word[1])
    result.append(latex( abs(integrate(v,(t,0,v0[0])))+abs(integrate(v,(t,v0[0],red_word[2]))) ))
    return result 

def p33_dint_particleacc(red_word):#3803857,36
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    a = 2*t+ red_word[0]
    v0 = -red_word[1]
    tt = [0,red_word[2]]
    #
    v = integrate(a,t)
    result.append(latex( v ))
    result.append(str( v.subs(t,0) ))
    c = - red_word[1]- v.subs(t,0)
    result.append(str( c ))
    v = v+c
    result.append(latex( v ))
    result.append('z')
    result.append('-z')
    tfa = solve(t-red_word[9]/t-red_word[8])[1]
    result.append(str(tfa))
    result.append(str(red_word[9]/tfa))
    result.append(str(-tfa))
    result.append(str(red_word[9]/tfa))
    result.append(str(red_word[9]/tfa))
    result.append('-1/3')
    result.append(str( red_word[8]/2 ))
    result.append(str( red_word[9] ))
    result.append('1/3')
    result.append(str( red_word[8]/2 ))
    result.append(str( red_word[9] ))
    result.append(str( abs(integrate(v,(t,0,red_word[-1])))+abs(integrate(v,(t,red_word[-1],red_word[-2]))) ))
    return result 

if __name__ == '__main__':
    red_word = [6,16,5,6,6,16,5,5,6,16,6,16,6,16,8,2,2,5,6,16,5,2,5,5,6,16,2,6,16,5,6,16,2,2,5,2]
    for i in p33_dint_particleacc(red_word):
        print(i)
