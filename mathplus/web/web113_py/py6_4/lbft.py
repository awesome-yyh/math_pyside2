# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_z_fww(red_word):
    red_word = list(map(float,red_word))
    result = []
    #
    F = red_word[0]*9.8
    W = F*red_word[1]
    w2 = red_word[7]*red_word[8]
    result.append(str(F))
    result.append(str(F))
    result.append(str(W))
    result.append(str(w2))
    return result

def p6_4_lbft(red_word):
    red_word = list(map(float,red_word))
    result = []
    result.append(str(red_word[0]*red_word[1]))
    return result

if __name__ == '__main__':
    red_word = [ 1.2,0.5,15,6,1.2,0.5,15,15,6] # 713964, 2
    for i in p6_4_z_fww(red_word):
        print(i)
