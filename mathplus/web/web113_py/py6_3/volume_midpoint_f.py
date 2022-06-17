# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_3_volume_midpoint_f(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    n = 5;
    y = (red_word[0]+red_word[1]*x**3)**(1/2);
    x0 = 0; x1 = 1;
    ##
    delta = (x1-x0)/n;
    xs = np.arange(x0+delta/2, x1+delta/2, delta)
    ssum = 0
    for i in xs:
        ssum += delta * i * y.subs(x,i)
    v = 2 * pi * ssum
    result.append(str(round(float(v),2)))
    return result

if __name__ == '__main__':
    red_word = [2,7];# 1817437,2
    for i in p6_3_volume_midpoint_f(red_word):
        print(i)

