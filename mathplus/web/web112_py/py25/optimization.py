# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p25_product(red_word):#3804422,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( sqrt(red_word[0]) ))
    result.append(str( sqrt(red_word[0]) ))    
    return result 

def p25_rectangle(red_word):#3803834,6
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append(str( red_word[2] ))
    result.append(str( red_word[2] ))
    result.append(str( red_word[4] ))
    result.append(str( -2 ))
    result.append(str( red_word[4] ))
    result.append(str( red_word[4] ))
    result.append(str( red_word[4] ))
    return result 

def p25_farmer(red_word):#3803326,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append('xy')
    result.append('5x+2y=red'.replace('red',str(red_word[0])))
    A = x/2*(red_word[0]-5*x)
    result.append(latex( A ))
    result.append(str( A.subs(x,solve(diff(A))[0]) ))
    return result 

def p25_gmanager(red_word):#3804348,5
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    result.append('100-x')
    x2 = -red_word[2]
    result.append(str( x2 ))
    x1 = red_word[2]*100- red_word[0]
    result.append(str( x1 ))
    R = x2*x**2+x1*x+red_word[0]*100
    dR = diff(R)
    result.append(str( dR ))
    dR0 = solve(dR)[0]
    result.append(str( dR0 ))
    result.append(str( (red_word[0]+red_word[2]*x).subs(x,dR0) ))
    return result 

def p25_gclosest(red_word):#3804481,24
    red_word = list(map(int,red_word))
    y = symbols('y')
    result = []
    #
    result.append('\\frac{y^2}{s0}'.replace('s0',str(red_word[0])))
    result.append('\\frac{y}{3}'.replace('s0',str(red_word[0]/2)))
    fp = 2*(1/red_word[0]*y**2- red_word[1])*(y/red_word[0]*2+2*(y- red_word[2]))
    result.append(str( simplify(fp)))
    result.append(str( red_word[11] ))
    result.append(str( (1/red_word[0]*y**2).subs(y,red_word[11]) ))
    result.append(str( (1/red_word[0]*y**2).subs(y,red_word[11]) ))
    result.append(str( red_word[11] ))
    return result 

if __name__ == '__main__':
    red_word = [6,3,12,3,12,3,12,6,6,3,12,6,3,12,6,3,12,6,6,6,6,6,3,12];
    for i in p25_gclosest(red_word):
        print(i)
