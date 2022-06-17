# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p05_smlimit():#3800905
    #
    result = []
    result.append( r'close to 7(red0)' )
    result.append( r'yes, hole at...' )
    return result

def p05_s3limit():#3802006
    #
    result = []
    result.append( r'2 duan after up' )
    return result

def p05_soo():#3801715
    #
    result = []
    result.append( r'-oo' )
    return result

def p05_soolog():#3801996
    #
    result = []
    result.append( r'-oo' )
    return result

if __name__ == '__main__':
    for i in p05_soolog():
        print(i)