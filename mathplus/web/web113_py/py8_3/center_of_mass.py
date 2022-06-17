# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_f_point(red_word):#806432,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    aa = [red_word[1], red_word[2]];ro= red_word[0]; y1 = aa[1]/aa[0]*x; y2 = 0; xx = [0, aa[0]]; 
    return p8_3_center_f(ro,y1,y2,xx)

def p8_3_center_f(ro,y1,y2,xx):
    result = []
    x,t = symbols('x t')
    ##
    xa = xx[0]; xb = xx[1];
    A = integrate(y1-y2,(x,xa,xb));
    Mx = ro * integrate(1/2 * (y1**2-y2**2),(x, xa, xb));
    My = ro * integrate(x*(y1-y2), (x,xa, xb));
    M =ro * A;
    xb = My / M;
    yb = Mx / M;
    result.append(str(Mx))
    result.append(str(My))
    result.append(str(xb))
    result.append(str(yb))
    return result

if __name__ == '__main__':
    red_word = [3,3,2];
    red_word = list(map(int,red_word))
    for i in p8_3_f_point(red_word):
        print(i)
