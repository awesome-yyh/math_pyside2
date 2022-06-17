# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from math import ceil

def p7_7_midpoint(red_word):#872859,12
    red_word1 = list(map(float,red_word[0:-3]))
    result = []
    x = symbols('x')
    #
    s = np.arange(0,3.6,0.4)
    f = [red_word1[0], red_word1[2], red_word1[4], red_word1[6], red_word[8], 
    red_word1[1], red_word1[3], red_word1[5], red_word1[7]]
    red_word2 = list(map(float,red_word[-2:]))
    f2x0 = -red_word2[-2]; f2x1 = red_word2[-1];
	#
    lens = len(s);
    delta = abs(s[2]-s[0]);
    xs = np.arange(2,lens+1,2)
    ssum = 0
    for i in xs:
    	ssum += f[i-1]
    ms = delta * ssum
    result.append(str(round(ms,2)))

    k = [abs(f2x0), abs(f2x1)]
    k = max(k)
    n = (lens-1)/2;
    e = k * (s[lens-1]-s[0])**3 / (24*n**2)
    result.append(str(round(e,4)))

    return result

if __name__ == '__main__':
    red_word = ['6.8','8.4','8.9','7.1','8.3','7.2','7.4','7.4','7.1','-','5','2']
    for i in p7_7_simpson_large_n(red_word):
        print(i)

# clear
# %sÊÇ´® fÊÇÖµ
# s = 0:0.4:3.2;
# f = [7.6 6.3 8.1 8.5 8.8 7.4 7.9 7.9 7.2
#     ];
