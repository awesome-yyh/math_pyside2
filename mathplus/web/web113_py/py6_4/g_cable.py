# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_4_g_cable(red_word):#1291120,5
    red_word = list(map(float,red_word))
    result = []
    x= symbols('x')
    #
    xi = red_word[2]
    shang = red_word[1]
    result.append(str(xi))
    ia = integrate(xi*x,x)
    result.append(latex(ia))
    s = integrate(xi*x,(x,0,shang))
    #
    result.append(str(round(s,2)))
    return result

def p6_4_g_Hooke(red_word):#708944,18
    red_word = list(map(float,red_word))
    result = []
    x= symbols('x')
    #
    result.append(str( red_word[7]/100 ))
    result.append(str( red_word[0] ))
    result.append(str( red_word[0]/red_word[7]*100 ))
    result.append(str( (red_word[4]-red_word[1])/100 ))
    s = (((red_word[4]-red_word[1])/100)**2 - red_word[-1]**2)* red_word[-2]
    result.append(str( round(s,4) ))
    return result

def p6_4_qiu3(red_word):#1875548,3,1.5
    red_word = list(map(float,red_word))
    result = []
    #
    r = red_word[0]
    h = red_word[1]
    #
    v = 4/3*pi*r**3
    m = v*1000
    f = m*9.8
    w = f*(r+h)
    result.append(str( round(float(w),2) ))
    return result

if __name__ == '__main__':
    red_word = [3,1.5] 
    for i in p6_4_qiu3(red_word):
        print(i)

# def p6_4_lbft(red_word):
#     red_word = list(map(float,red_word))
#     result = []
#     result.append(str(red_word[0]*red_word[1]))
#     return result

# if __name__ == '__main__':
#     red_word = [100,200] # 713964, 2
#     for i in p6_4_lbft(red_word):
#         print(i)
