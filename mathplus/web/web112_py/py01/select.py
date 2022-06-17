# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_sabs():#3798905
    #
    result = []
    result.append( 'ping up' )
    return result

def p01_sd2():#3799405
    #
    result = []
    result.append( 'odd' )
    return result

def p01_sfgh():#3798232
    #
    result = []
    result.append( 'h f g' )
    return result

def p01_scosdsin():#3798858
    result = []
    #
    result.append( r'pi/2+2npi' )
    return result

def p01_ssqrt(red_word):#3799232,2
    #
    result = []
    result.append( '-s1 righ'.replace('s1',str(red_word[1])) )
    return result

if __name__ == '__main__':
    red_word = [4,5];
    for i in p01_ssqrt(red_word):
        print(i)