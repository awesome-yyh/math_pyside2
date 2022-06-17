# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_midpoint(red_word):
    red_word = list(map(float,red_word))
    result = []
    h = symbols('h')
    # 
    x = np.arange(red_word[0],red_word[1]+red_word[3]-red_word[2],red_word[3]-red_word[2])
    f = red_word[11:]
    n = 4
    l = len(f);
    xs = np.arange(1+(l-1)/n/2, (l-1)/n+l-(l-1)/n/2, (l-1)/n)
    s = 0
    for i in xs:
        s += f[int(i)-1]
    w = (x[l-1]-x[0]) / n * s ;
    #
    result.append(str(abs(round(w,2))))
    return result

if __name__ == '__main__':
    red_word = [2,18,2,4,6,8,10,12,14,16,18,5,5.5,7.1,8.8,9.8,8.3,6.5,5.3,3.9]
    for i in p6_4_midpoint(red_word):
        print(i)
