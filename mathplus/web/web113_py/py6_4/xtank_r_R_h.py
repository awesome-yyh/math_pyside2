# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_tank_a_b_c(red_word):
    red_word = list(map(float,red_word))
    result = []
    h = symbols('h')
    # 
    a = red_word[0]; #矩形面的高
    b = red_word[1]; #矩形面的宽
    c = red_word[2]; #三角形面的长
    ro = 62.5;
    ## 计算
    delta = b * c*h/a * (a-h) * ro;
    w = integrate(delta, (h,0, a));
    #
    result.append(str(abs(round(w))))
    return result

if __name__ == '__main__':
    red_word = [4,6,14]
    for i in p6_4_tank_a_b_c(red_word):
        print(i)


# clear
# syms hp hs rs
# %% 参数
# r = 5;
# R = 10;
# h = 12;
# ro = 62.5;
# %% 计算
# hp = solve(r/hp - R/(hp+h));
# H = hp + h;
# hsp = H - hs;
# rs = solve(rs/hsp - R/H);
# s = pi * rs^2;
# w = int(s*ro*hs,0, h);
# format long
# fprintf('%.2f\n', w)
# clipboard('copy',double(round(w*100)/100))
# disp('结果已在剪贴板')