# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p10_2_point_h_v_t2t3(red_word):#806453,3
    red_word = list(map(int,red_word))
    t = symbols('t')
    x = red_word[0]-t**2;  y = t**3-red_word[1]*t;flag = 2;
    return p10_2_point_h_v(x,y,flag)

def p10_2_point_h_v_t3t2(red_word):#807950,2
    red_word = list(map(int,red_word))
    t = symbols('t')
    x = 2*t**3+3*t**2-red_word[0]*t; y = 2*t**3+3*t**2+red_word[1];flag = 3;
    return p10_2_point_h_v(x,y,flag)

def p10_2_point_h_v(x,y,flag):
    result = []
    t = symbols('t')
    ##
    sdy = solve(diff(y));
    sdx = solve(diff(x))

    tt = sdy[0];
    tyx = x.subs(t,tt);
    tyy = y.subs(t,tt);
    result.append(str(tyx))
    result.append(str(tyy))
    if len(sdy) == 2:
        tt1 = sdy[1];
        tyx = x.subs(t,tt1);
        tyy = y.subs(t,tt1);
        result.append(str(tyx))
        result.append(str(tyy))

    tx = sdx[0];
    txx = x.subs(t,tx);
    txy = y.subs(t,tx);
    result.append(str(txx))
    result.append(str(txy))

    if len(sdy) == 2 and flag ==3:
        tx1 = sdx[1];
        txx = x.subs(t,tx1);
        txy = y.subs(t,tx1);
        result.append(str(txx))
        result.append(str(txy))
        result.append('add + -')

    return result

if __name__ == '__main__':
    red_word = [12,48]; 
    for i in p10_2_point_h_v_t2t3(red_word):
        print(i)



# x = t**2-t; y = 2*sqrt(t);
# x = 5*cos(t); y = sin(2*t);
# x = cos(3*t); y = 9*sin(t);# 0 -y的系数 0 y的系数,, 1 -* 1 0 1 *,*是 subs(y,pi/3)   依照下面，手动算的txy
