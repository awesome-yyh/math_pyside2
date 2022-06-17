# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_2_tetrahedron(red_word):
    red_word = list(map(float,red_word))
    result = []
    z = symbols('z')
    ##
    l1 = red_word[0]
    l2 = red_word[1]
    l3 = red_word[2]

    h = l1/l3 * (l3-z);
    b = l2/l3 * (l3-z);
    A = 1/2 * b * h;
    s = integrate(A,(z,0,l3))
    result.append(latex(abs(s)))
    return result

def p6_2_squares_yare(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    yf = sqrt((red_word[0]-x)/red_word[1])
    #
    a = (2*yf)**2
    x1 = solve(a,x)
    V = integrate(a,(x,0,int(x1[0])))
    result.append(latex(V))
    return result

if __name__ == '__main__':
    red_word = [4,2];
    for i in p6_2_squares_yare(red_word):
        print(i)