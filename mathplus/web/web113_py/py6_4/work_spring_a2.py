# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_work_spring_a2(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    # 
    w0 =       red_word[0]
    natural = red_word[1]
    l1 =      red_word[2]
    ## (a)参数
    la1 = red_word[3]
    la2 = red_word[4]
    f =   red_word[5] #(b)参数
    ## (a)
    x1 = (l1 -natural) / 100
    k = 2*w0 / x1**2
    xa1 = (la1-natural)/100
    xa2 = (la2-natural)/100
    wa = integrate(k*x, (x,xa1, xa2))
    ## (b)
    x = f / k * 100 #化厘米

    result.append(str(abs(round(wa,2))))
    result.append(str(abs(round(x,2))))
    return result

if __name__ == '__main__':
    red_word = [4,28,41,32,37,15]
    for i in p6_4_work_spring_a2(red_word):
        print(i)
