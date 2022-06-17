# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p01_Biologists(red_word):#3799249,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    # 
    T = '\\frac{1}{s0}\\left(N-113\\right)+s1'
    result.append(T.replace('s0',str((red_word[0]-113)/10)).replace('s1',str(red_word[0]-113)) )
    #
    result.append(str(10/(red_word[0]-113)))
    #
    Tx = 10/(red_word[0]-113)*(x-113)+red_word[0]-113
    result.append(str(round(Tx.subs(x,red_word[1]))))
    return result

    solve(Ax)
    #
    return result

if __name__ == '__main__':
    red_word = [183,190];
    for i in p01_Biologists(red_word):
        print(i)