# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_2_selectab(red_word):
    red_word = list(map(int,red_word))
    result = []
    
    result.append('double, other = no double')
    result.append('\\frac{ss}{2}\\cdot h\cdot \pi \cdot r^2'.replace('ss',str(red_word[0]**2*red_word[1])))
    return result

if __name__ == '__main__':
    red_word = [7,7];
    for i in p6_2_selectab(red_word):
        print(i)
