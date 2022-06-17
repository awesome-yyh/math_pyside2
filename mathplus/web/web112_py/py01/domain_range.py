# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_DRsqrt(red_word):#3798618,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    f = sqrt(red_word[0]-x**2)
    #
    return p01_DR(f,x,result)

def p01_DR(f,x,result):
    ## domain
    dom = '\\left[s0,s1\\right]'
    ss = solve(f)
    result.append( dom.replace('s0',str(ss[0])).replace('s1',str(ss[1])) )
    ## range
    df = diff(f)
    df0 = solve(df)
    xxx = ss+df0
    v = []
    for x0 in xxx:
        v.append(f.subs(x,x0))
    vmax = max(v);vmin = min(v);
    rrange = '\\left[min,max\\right]'
    result.append( rrange.replace('min',str(vmin)).replace('max',str(vmax)))
    return result

if __name__ == '__main__':
    red_word = [9];
    for i in p01_DRsqrt(red_word):
        print(i)