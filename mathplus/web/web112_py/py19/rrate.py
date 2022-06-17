# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p19_gawl(red_word):#3803074,4
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    result.append( 'dw/dt' )
    result.append( 'w' )
    result.append(str( red_word[2] ))
    result.append(str( red_word[3] ))
    result.append(str( red_word[1] ))
    result.append(str( red_word[0] ))
    result.append(str( red_word[2]*red_word[1]+red_word[3]*red_word[0] ))
    return result 

def p19_oil(red_word):#3802716,1
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    result.append( '2\\pi r' )
    result.append(str( red_word[0]*2 )+'\\pi')
    return result 

def p19_sphere(red_word):#3802916,2
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    result.append(str( 4*(red_word[1]/2)**2*red_word[0] )+'\\pi')
    return result 

def p19_gcars(red_word):#3802439,8
    red_word1 = list(map(int,red_word[0:2]))
    red_word2 = list(map(int,red_word[3:]))
    hours = red_word[2]
    t = symbols('t')
    result = []
    #
    result.append('x^2+y^2')
    result.append('dz/dt')
    result.append('2*y')
    result.append('1/z')
    result.append('y')
    result.append(str( red_word2[3] ))
    z = sqrt(red_word2[3]**2+red_word2[1]**2)
    result.append(str( z ))
    result.append(str( red_word1[0] ))
    result.append(str( red_word1[1] ))
    result.append(str( (red_word2[3]*red_word1[0]+red_word2[1]*red_word1[1])/z ))
    return result 

def p19_gspotlight(red_word):#3802804,1
    red_word = list(map(float,red_word))
    t = symbols('t')
    result = []
    #
    result.append('y/12')
    result.append('24')
    result.append('-1')
    result.append('-24*x^(-2)')
    result.append(str( red_word[0] ))
    result.append(str( round(red_word[0]*(-24)/64,2) ))
    result.append(str( round(red_word[0]*(-24)/64,2) ))
    return result 

def p19_trough(red_word):#3803623,4
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    result.append('b/h')
    result.append(str( red_word[0] ))
    result.append(str( red_word[0]/2 ))
    result.append(str( red_word[0]/2*3 )+'h^2')
    result.append(str( red_word[0]/2*3*2 )+'h')
    h = red_word[2]/12
    result.append(str( h ))
    result.append(str( solve(red_word[3]-red_word[0]/2*3*2*h*t)[0] ))
    return result 

def p19_gravel(red_word):#3804351,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    dvdt = red_word[0]
    h = red_word[1]
    result.append(str( round(solve(1/4*pi*h**2*x-dvdt)[0],3) ))
    return result 

if __name__ == '__main__':
    red_word = [10,8];
    for i in p19_gravel(red_word):
        print(i)
