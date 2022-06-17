# 返回元素为字符串的list
# 参数是[100,800]的list
import numpy as np
from sympy import *

def p6_5_average_Midpoint(red_word):
    red_word = list(map(float,red_word))
    result = []
    ##
    n = 3; #固定的，题中没写
    x = np.arange(20,50+5,5)
    f = red_word
    ## 计算
    l = len(f);
    xs = np.arange(1+(l-1)/n/2, l, (l-1)/n)
    w = 0
    for i in xs:
        w += (x[l-1]-x[0]) / n * f[int(i)-1]
    s = w/(x[l-1]-x[0])
    result.append(str(float(s)))
    return result

if __name__ == '__main__':
    red_word = [40,37,27,25,28,43,53] # 1816325,7
    for i in p6_5_average_Midpoint(red_word):
        print(i)
