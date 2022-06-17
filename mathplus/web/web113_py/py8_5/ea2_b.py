# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *

def p8_5_ea2_b(red_word): #自变量len为2的list（红字）
    red_word = list(map(float,red_word))
    t = symbols('t')
    result = []
    a1 = red_word[0]
    a2 = red_word[1]
    ##
    y1 = 1/1000*exp(-t/1000);
    i1 = integrate(y1,(t,0,a1));
    i2 = integrate(y1,(t,a2,oo));
    result = [str(round(float(i1),3)), str(round(float(i2),3)), '693.1']

    return result

if __name__ == '__main__':
    red_word = [400,600]
    for i in p8_5_ea2_b(red_word):
        print(i)
    