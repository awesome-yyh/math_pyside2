# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p05_cardiac(red_word):#3801214,5
    red_word = list(map(int,red_word))
    result = []

    result.append(str(round( (red_word[3]- red_word[0])/6 ,1)))
    result.append(str(round( (red_word[3]- red_word[1])/4 ,2)))
    result.append(str(round( (red_word[3]- red_word[2])/2 ,1)))
    result.append(str(round( (red_word[4]- red_word[3])/2 ,1)))
    return result

if __name__ == '__main__':
    red_word = [2550,2690,2830,2967,3107];
    for i in p05_cardiac(red_word):
        print(i)