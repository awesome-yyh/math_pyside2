# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p02_du():#3806472
    #
    result = []
    result.append( '3' )
    return result

def p02_qdu():#3805869
    #
    result = []
    result.append( '1' )
    return result

def p02_du6():#3805882
    #
    result = []
    result.append( '1' )
    result.append( '1' )
    result.append( '0' )
    result.append( '\\operatorname{UNDEFINED}' )
    result.append( '\\operatorname{UNDEFINED}' )
    result.append( '0' )
    return result

def p02_scos():#3805947
    #
    result = []
    result.append( 'down up down up y-right' )
    return result

if __name__ == '__main__':
    for i in p02_scos():
        print(i)