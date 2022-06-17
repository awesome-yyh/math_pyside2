# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *

def p6_1_gR_L(red_word): #自变量len为2的list（红字）
    red_word = list(map(int,red_word))
    y = symbols('y')
    result = []
    int3 = -1/6*y**3
    x1 = y+red_word[0]
    x2 = ((y**2)-red_word[1])/2
    result1 = red_word[2]-red_word[0]
    result2 = red_word[3]-red_word[0]
    result.append(str(result1))
    result.append(str(result2))
    result.append(latex(x2))
    result.append(latex(x1-x2))
    result.append(latex(integrate(x1-x2,y)))
    result.append(str(int3.subs(y,result2)))
    result.append((str(int3.subs(y,result1))))
    result.append(str(integrate(x1-x2,(y,result1,result2))))

    return result

if __name__ == '__main__':
    red_word = [4,40,-2,12,20,4,-6,8,4,32,192,18,144]
    for i in p6_1_gR_L(red_word):
        print(i)
    