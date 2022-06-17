# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p26_farmer(red_word):#3803474,1
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    #
    red_word = red_word[0]*10**6
    f = 3*x+2*(red_word/x)
    mx = abs(solve(diff(f))[0])
    result.append(str( mx ))
    result.append(str( red_word/mx ))    
    return result 

def p26_gmaterial(red_word):#3803567,7
    red_word = list(map(int,red_word))
    x,b = symbols('x b')
    result = []
    #
    result.append(str( 4 ))
    result.append(str( 4*b ))
    result.append(str( red_word[6] ))
    result.append(str( 4 ))
    result.append(str( red_word[6] ))
    result.append(str( 3/4 ))
    v = red_word[6]*x-1/4*x**3
    dv = diff(v)
    dvx = solve(dv)[1]
    result.append(str( dvx ))
    result.append(str( v.subs(x,dvx) ))
    return result 

def p26_point1(red_word):#3804559,2
    red_word = list(map(int,red_word))
    x,b = symbols('x b')
    result = []
    #
    y = red_word[0]*x+red_word[1]
    xy = [0,0]
    return p21_closest(y,xy,x,result)    
    
def p21_closest(y,xy,x,result):
    ##
    x0 = xy[0];y0 = xy[1];
    L2 = (x-x0)**2+(y-y0)**2;
    x1 = solve(diff(L2))
    y1 = y.subs(x,x1[0])
    result.append(str( x1[0] ))
    result.append(str( y1 ))
    return result 

def p26_poster(red_word):#3803663,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    area = red_word[2];
    h = red_word[0];
    s = red_word[1];
    ##
    y = (x+s*2)*(area/x+h*2)
    ##
    xx = max(solve(diff(y)))
    yy = area/xx
    result.append(str( xx+s*2 ))
    result.append(str( yy+h*2 ))
    return result 

def p26_posterbs(red_word):#3803505,3
    red_word = list(map(int,red_word))
    w = symbols('w')
    result = []
    #
    area = red_word[0];
    ms = red_word[1];
    mh = red_word[2];
    ##
    y = (w+2*ms)*(area/w+ms+mh)
    ##
    xx = max(solve(diff(y,w)))
    yy = area/xx
    result.append(latex( xx ))
    result.append(latex( yy ))
    return result 

if __name__ == '__main__':
    red_word = [240,1,2];
    for i in p26_posterbs(red_word):
        print(i)
