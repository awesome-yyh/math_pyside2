# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_select_cable(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    s = integrate(red_word[0]*x,(x,0,red_word[2]))+red_word[1]*red_word[2]
    #
    result.append('double * x +..')
    result.append('double * x +..')
    result.append(str(abs(round(s,2))))
    return result

def p6_4_select_bucket(red_word): #657142,5
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    ia = red_word[2]-x/10
    s = integrate(ia,(x,0,red_word[1]))+red_word[0]*red_word[1]
    #
    result.append('/10 + ..')
    result.append('/10 + ..')
    result.append(str(abs(round(s,2))))
    return result

def p6_4_tank_r_R_h(red_word): #1875559,3
    red_word = list(map(float,red_word))
    result = []
    hp, hs, rs = symbols('hp hs rs')
    # 
    r = red_word[0];
    R = red_word[1];
    h = red_word[2];
    ro = 62.5;
    #
    hp = solve(r/hp - R/(hp+h),hp)[0]
    H = hp + h;
    hsp = H - hs;
    rs = solve(rs/hsp - R/H,rs)[0]
    s = pi * rs**2;
    w = integrate(s*ro*hs,(hs,0, h))
    #
    result.append(str(abs(round(float(w),2))))
    return result


def p6_4_s_cable(red_word): #1387513,3
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    # 
    w = red_word[0]; #lbs
    l = red_word[1]; #ft
    ll = red_word[2]; #
    #
    delta = w/l;
    s = integrate(delta*x, (x,0, l))
    #
    result.append(str(abs(round(float(s),2))))
    return result

def p6_4_gas(red_word): #1387513,3
    red_word = list(map(int,red_word))
    result = []
    v = symbols('v')
    # 
    ro = red_word[0]; #lb/in^2
    v1 = red_word[1]; 
    v2 = red_word[2]; #in^3
    #
    ro = ro*144;
    v1 = v1 / 1728; v2 = v2 / 1728;
    k = ro*v1**1.4;
    s = integrate((v**(-7/5)))
    w = k * (s.subs(v,v2) - s.subs(v,v1))
    #
    result.append(str(abs(round(float(w),2))))
    return result

if __name__ == '__main__':
    red_word = [200,100,500]
    for i in p6_4_s_cable(red_word):
        print(i)
