from sympy import *
import numpy as np
from scipy.integrate import quad


def p11_2_sum_dn(red_word):
    red_word = list(map(int,red_word))
    result = []
    n = symbols('n')
    ##
    a = red_word[0]/red_word[1]**n
    s = summation(a,(n,red_word[2],oo))
    #
    result.append(str(s))
    return result

def p11_2_t_sum_dnkh(red_word):
    red_word = list(map(int,red_word))
    result = []
    n = symbols('n')
    ##
    a = red_word[0]/(n*(n+red_word[1]))
    result.append('sum '+str(a)+', n='+str(red_word[2])+' to infinity')
    result.append('https://www.wolframalpha.com/')
    #
    return result

def p11_2_t_sum_c(red_word):
    red_word = list(map(int,red_word))
    result = []
    n,c = symbols('n c')
    ##
    y = (1+c)**(-n)
    ss = red_word[0]
    tt = solve((1/(1+c))**2-ss*(1-1/(1+c)),c)
    result.append(latex(tt[0]))
    print(33/10+23/990)
    return result

def p11_2_t_sum_d(red_word):
    red_word = list(map(int,red_word))
    result = []
    n = symbols('n')
    ##
    a = red_word[0]**(n-1)/red_word[1]**n
    s = summation(a,(n,1,oo))
    result.append(str(s))
    return result

def p11_2_t_consum_d(red_word):
    red_word = list(map(int,red_word))
    result = []
    n = symbols('n')
    ##
    a = (1+red_word[0]**n)/red_word[1]**n
    s = summation(a,(n,1,oo))
    result.append('con')
    result.append(str(s))
    return result

def p11_2_s_xs2f(red_word):
    red_word = list(map(float,red_word))
    result = []
    ##
    result.append(str(red_word[1]))
    result.append('1/100')
    result.append(str(red_word[1])+'/1000')
    result.append('1/100')
    result.append('10')
    result.append(str(red_word[1]))
    result.append(str(int((red_word[-1]*99+red_word[1])/10))+'/99')
    
    return result

if __name__ == '__main__':
    red_word = [-5,8]
    for i in p11_2_t_sum_d(red_word):
        print(i)


# from sympy import *
# n = symbols('n')
# ## 等差等比数列求和
# # an = [2 1 1/2];
# # an = [1 1/(4*2**(1/7)) 1/(9*3**(1/7))];
# # an = [31 3.1 0.31];
# # an = [6 0.6 0.06];
# # an = [0.1 0.01 0.001];
# # an = [0.85 0.0085 0.000085];
# # an = [0.654 0.000654 0.000000654];
# # an = [0.049 0.00049 0.0000049]; #36
# # an = [0.019 0.000015 0.000000015]; #036循环
# # an = [0.0153 0.0000153 0.0000000153];
# an = [0.0091, 0.000091, 0.00000091];
# # an = [0.12345 0.0000012345 0.000000000012345];
# # an = [0.54321 0.0000054321 0.000000000054321];
# ##
# if ((abs(an[1]/an[0] - an[2]/an[1])) < 10**(-15)): #等比
#     q = an[1]/an[0];
#     sn = an[0] * (1-q**n)/(1-q);
# elif abs(an[1]-an[0]) == abs(an[2]-an[1]): #等差
#     sn = n*an[0] + n*(n-1)/2;
# else:
#     print('不造')
# print(sn)
# ansa = limit(sn,n,oo)
# print(ansa)