# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_work_spring_cm(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    # w = 1/2 * k * x^2; 
    ## 参数
    F0 = red_word[1];
    L0 = red_word[0]; #自然长度
    L1 = red_word[2]; #单位都是厘米
    lw0 = red_word[3];
    lw1 = red_word[4];
    ## 计算
    L0 = L0/100;
    L1 = L1/100;
    lw0 = lw0/100;
    lw1 = lw1/100;
    K = F0 / (L1-L0);
    f = K * x ;
    w = integrate(f, (x,lw0-L0, lw1-L0));
    #
    result.append(str(abs(round(w,3))))
    return result

def p6_4_s_cm(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    # w = 1/2 * k * x^2; 
    ## 参数
    F0 = red_word[0];
    L0 = red_word[1]; #自然长度
    L1 = red_word[2]; #单位都是厘米
    lw0 = red_word[3];
    lw1 = red_word[4];
    ## 计算
    L0 = L0/100;
    L1 = L1/100;
    lw0 = lw0/100;
    lw1 = lw1/100;
    K = F0 / (L1-L0);
    f = K * x ;
    w = integrate(f, (x,lw0-L0, lw1-L0));
    #
    result.append(str(abs(round(w,3))))
    return result

if __name__ == '__main__':
    red_word = [35,20,28,28,36]
    for i in p6_4_s_cm(red_word):
        print(i)
