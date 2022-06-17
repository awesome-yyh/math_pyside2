# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
import pyperclip

def p6_2_volume_rotate_x_none():
    x = symbols('x')
    # 
    # y1 = 2*sqrt(25-x**2); y2 = 0; xx = [1, 3]; d = 0;
    # y1 = 4/x; y2 = 0; xx = [1, 3]; d = -1;
    y1 = x**3; y2 = 27; xx = solve(y1-y2);print(xx); d =0;xx=[0, xx[0]]
    return p6_2_volume_rotate_x(y1,y2,xx,d)

def p6_2_volume_rotate_x2(red_word):
    x = symbols('x')
    # 
    y1 = -x**2+red_word[0]*x-red_word[1]; y2 = 0; xx = solve(y1-y2); d = 0;
    return p6_2_volume_rotate_x(y1,y2,xx,d)

def p6_2_volume_rotate_x(y1,y2,xx,d):
    result = []
    x = symbols('x')
    # 
    x0 = xx[0]; x1 = xx[1];
    a = pi * ((y1-d)**2 - (y2-d)**2);
    s = integrate(a, (x,x0, x1))
    ls = latex(abs(s)).replace('log','ln')
    result.append(ls)
    return result

if __name__ == '__main__':
    for i in p6_2_volume_rotate_x_none():
        print(i)
        pyperclip.copy(i)
        print('已复制')

# if __name__ == '__main__':
#     red_word = [10, 24];# 3875268,2
#     for i in p6_2_volume_rotate_x2(red_word):
#         print(i)
#         pyperclip.copy(i)
#         print('已复制')
