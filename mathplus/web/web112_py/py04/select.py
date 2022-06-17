# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p04_sfig():#3798643
    #
    result = []
    result.append( 'horizontal' )
    result.append( r'\left[-2,0\right],\left[0,2\right]' )
    result.append( r'\left[-3,3\right]' )
    result.append( '0' )
    result.append( '-1' )
    return result

def p04_slog():#3799190
    #
    result = []
    result.append( 'up left' )
    result.append( 'down 4' )
    return result

if __name__ == '__main__':
    for i in p04_slog():
        print(i)