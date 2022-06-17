# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_hydrostatic_simpson(red_word):
    red_word = list(map(float,red_word))
    result = []
    x= symbols('x')
    #
    #s是串 f是值
    s = np.arange(2,5+0.5,0.5)
    f = red_word
    ##
    lens = len(s);
    delta = abs(s[lens-1]-s[0]) / (lens-1);
    f4 = np.arange(2,lens+1,2)
    f2 = np.arange(3,lens,2)
    sf4 = 0
    for i in f4:
        sf4 += 4*s[int(i)-1]*f[int(i)-1]
    sf2 = 0
    for i in f2:
        sf2 += 2*s[int(i)-1]*f[int(i)-1]
    sim = delta/3 * (s[0]*f[0] + sf4 + sf2 + s[lens-1]*f[lens-1]);
    F = sim * 1000 * 9.8;
    #
    result.append(str(round(F,2)))
    return result

if __name__ == '__main__':
    red_word = [0,0.9,1.6,2.1,2.9,3.2,3.9] #806464,7
    for i in p8_3_hydrostatic_simpson(red_word):
        print(i)
