# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p05_ave_v(red_word):#3801808,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    y = red_word[0]*x-16*x**2
    result.append( str(round( (y.subs(x,2.5)-y.subs(x,2))/0.5,3)) )
    result.append( str(round( (y.subs(x,2.1)-y.subs(x,2))/0.1,3)) )
    result.append( str(round( (y.subs(x,2.05)-y.subs(x,2))/0.05,3)) )
    result.append( str(round( (y.subs(x,2.01)-y.subs(x,2))/0.01,3)) )
    result.append( str(round( diff(y).subs(x,2),3)) ) 
    return result

def p05_ave_v_sin(red_word):#3801322,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    y = red_word[0]*sin(pi*x)+red_word[1]*cos(pi*x)
    result.append( str(round( float((y.subs(x,2)-y.subs(x,1))/1),2)) )
    result.append( str(round( float((y.subs(x,1.1)-y.subs(x,1))/0.1),2)) )
    result.append( str(round( float((y.subs(x,1.01)-y.subs(x,1))/0.01),2)) )
    result.append( str(round( float((y.subs(x,1.001)-y.subs(x,1))/0.001),2)) )
    result.append( str(round( float(diff(y).subs(x,1)),3)) ) 
    return result

def p05_ave_v_gtank(red_word):#3801612
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    y = red_word[0]*sin(pi*x)+red_word[1]*cos(pi*x)
    result.append( str( red_word[1] ))
    result.append( str( -10 ))
    result.append( str(round(float( (red_word[1]-red_word[3])/(-10) ) ,2)) )
    result.append( str( red_word[2] ))
    result.append( str( -5 ))
    result.append( str(round(float( (red_word[2]-red_word[3])/(-5) ) ,2)) )
    result.append( str( red_word[4] ))
    result.append( str( 20 ))
    result.append( str(round(float( (red_word[4]-red_word[3])/(5) ) ,2)) )
    result.append( str( red_word[5] ))
    result.append( str( 25 ))
    result.append( str(round(float( (red_word[5]-red_word[3])/(10) ) ,2)) )
    result.append( str( red_word[6] ))
    result.append( str( 30 ))
    result.append( str(round(float( (red_word[6]-red_word[3])/(15) ) ,2)) )
    result.append( str( 10 ))
    result.append( str( 20 ))
    result.append( str(round(float( (red_word[4]-red_word[3])/(5) ) ,2)) )
    result.append( str( 2 ))
    result.append( str(round(float( ((red_word[2]-red_word[3])/(-5)+(red_word[4]-red_word[3])/(5))/2 ) ,2)) )
    return result

if __name__ == '__main__':
    red_word = [6000,4122,2628,1440,672,168,0]
    for i in p05_ave_v_gtank(red_word):
        print(i)