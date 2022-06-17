# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p18_particle(red_word):#4020903,2
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    f = t**3- red_word[0]*t**2 +red_word[1]*t
    dy = diff(f)
    result.append(latex( dy ))
    result.append(str( dy.subs(t,1) ))
    result.append( '\\operatorname{DNE}' )
    result.append( '\\left[0,\\infty \\right)' )
    result.append(str( f.subs(t,6) ))
    result.append( 'right right right' )
    at = diff(dy)
    result.append(latex( at ))
    result.append(str( at.subs(t,1) ))
    result.append( 's up' )
    aa = solve(at)
    result.append( '['+str(aa[0])+',oo)' )
    result.append( '[0,'+str(aa[0])+']' )
    return result 

def p18_height(red_word):#3802172,4
    red_word = list(map(float,red_word))
    t = symbols('t')
    result = []
    #
    h0 = red_word[0]
    v0 = red_word[1]
    h = red_word[2]+red_word[3]*t-4.9*t**2
    #
    v = diff(h)
    result.append(str( round(v.subs(t,2),3) ))
    result.append(str( round(v.subs(t,4),3) ))
    maxt = solve(v)
    result.append(str( round(maxt[0],3) ))
    result.append(str( round(h.subs(t,maxt[0]),3) ))
    ground = solve(h)
    result.append(str( round(ground[1],3) ))
    result.append(str( round(v.subs(t,ground[1]),3) ))
    return result 

def p18_sodium(red_word):#3802914,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    v = x**3
    vp = diff(v)
    result.append(str( vp.subs(x,red_word[0]) ))
    result.append('which the volume ... 5(red)')
    return result 

def p18_spherical(red_word):#3802972,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    v = 4*pi*x**2
    vp = diff(v)
    result.append(latex( vp.subs(x,red_word[0]) ))
    result.append(latex( vp.subs(x,red_word[1]) ))
    result.append(latex( vp.subs(x,red_word[2]) ))
    return result 

def p18_cost(red_word):#3802475,4
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    #
    v = red_word[0]+red_word[1]*x- red_word[2]*x**2+red_word[3]*x**3
    vp = diff(v)
    result.append(str( round(vp.subs(x,100),3) ))
    result.append('rate at ... are inc')
    result.append(str( round(v.subs(x,101)-v.subs(x,100),3) ))
    return result 

def p18_gtank(red_word):#3802496,16
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    v = red_word[2]*(1-t/red_word[3])**2
    vp = diff(v)
    result.append(str( vp ))
    result.append(str( vp.subs(t,5) ))
    result.append(str( vp.subs(t,10) ))
    result.append(str( vp.subs(t,20) ))
    result.append(str( vp.subs(t,50) ))
    result.append('beginning')
    result.append('0')
    result.append('end')
    result.append(str( red_word[1] ))
    return result 

def p18_Newton_Law(red_word):#3803105,5
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    #
    result.append('-2GmMr^{-3}')
    result.append('force')
    result.append('...inc,...dec')
    result.append(str( -1*red_word[0]*red_word[1]**3/red_word[3]**3 ))
    return result 

if __name__ == '__main__':
    red_word = [369,22,0.05,0.0002];
    for i in p18_cost(red_word):
        print(i)
