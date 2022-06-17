# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from math import ceil

def p7_7_midnight06(red_word):
    red_word = list(map(int,red_word))
    s = np.arange(0,6.5,0.5)
    f = []
    for i in np.arange(0,len(red_word)):
        if i%2 == 0:
            f.append(red_word[i])
    for i in np.arange(0,len(red_word)):
        if i%2 != 0:
            f.append(red_word[i])
    return simpson_point(s,f)

def p7_7_simpson_point18(red_word):
    red_word = list(map(float,red_word))
    s = np.arange(0,21,3)
    f = red_word
    return simpson_point(s,f)

def p7_7_simpson_point_gun(red_word):
    red_word = list(map(float,red_word))
    s = np.arange(0,5+0.5,0.5)
    f = [0]
    for i in np.arange(0,len(red_word)):
        if i%2 != 0:
            f.append(red_word[i])
    for i in np.arange(0,len(red_word)):
        if i%2 == 0:
            f.append(red_word[i])
    return simpson_point(s,f)
    #
def simpson_point(s,f):
    result = []
    lens = len(s);
    delta = abs(s[lens-1]-s[0]) / (lens-1);
    f4 = np.arange(2,lens+1,2)
    f2 = np.arange(3,lens,2)
    sf4 = 0
    for i in f4:
        sf4 += 4*f[i-1]
    sf2 = 0
    for i in f2:
        sf2 += 2*f[i-1]
    sim = delta/3 * (f[0] + sf4 + sf2 + f[lens-1])
    F = sim * 1000 * 9.8
    #
    result.append(str(round(float(sim),3)))
    return result

# if __name__ == '__main__':
#     red_word = [9.7,9.3,8.5,8,7.9,7.5,7.3]; #1816931,7
#     for i in p7_7_simpson_point18(red_word):
#         print(i)

if __name__ == '__main__':
    red_word = [1814,1616,1730,1624,1689,1670,1646,1744,1640,1884,1608,2056,1609]
    for i in p7_7_midnight06(red_word):
        print(i)