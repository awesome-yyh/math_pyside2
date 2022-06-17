# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p02_length_abx(red_word):#3806062,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    x = red_word[0] / cos( red_word[1]/red_word[2]*pi )
    result.append(str(round(float(x),6)))
    return result

if __name__ == '__main__':
    red_word = [24,5,12]; 
    for i in p02_length_abx(red_word):
        print(i)