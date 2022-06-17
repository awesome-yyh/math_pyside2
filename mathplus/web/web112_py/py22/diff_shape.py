# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p22_shape3(red_word):#3804353,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**3- red_word[0]*x**2- red_word[1]*x+red_word[2]
    df = diff(f)
    dfx = solve(df)
    inc = '\\left(-\\infty ,df0\\right),\\left(df1,\\infty \\right)'
    result.append(inc.replace('df0',str(dfx[0])).replace('df1',str(dfx[1])))
    dec = '\\left(df0,df1\\right)'
    result.append(dec.replace('df0',str(dfx[0])).replace('df1',str(dfx[1])))
    v = []
    for x0 in dfx:
        v.append(f.subs(x,x0))
    vmax = max(v);vmin = min(v);
    result.append(str( vmin ))
    result.append(str( vmax ))
    ddf = diff(df)
    ddfx = solve(ddf)
    result.append(str( ddfx[0] )+','+str( f.subs(x,ddfx[0]) ))
    up = '\\left(ddf0,\\infty \\right)'
    down = '\\left(-\\infty ,ddf0\\right)'
    result.append(up.replace('ddf0',str(ddfx[0])))
    result.append(down.replace('ddf0',str(ddfx[0])))
    return result 

def p22_local3(red_word):#3803428,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]+red_word[1]*x**2- red_word[2]*x**3
    df = diff(f)
    dfx = solve(df)
    v = []
    for x0 in dfx:
        v.append(f.subs(x,x0))
    vmax = max(v);vmin = min(v);
    result.append(str( vmax ))
    result.append(str( vmin ))
    return result 

def p22_criticalabc(red_word):#3803471,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**(red_word[0])*(x- red_word[1])**red_word[2]
    df = diff(f)
    dfx = solve(df)
    result.append(str( dfx[0] ))
    result.append(str( dfx[1] ))
    result.append(str( dfx[2] ))
    result.append(str( dfx[1] ))
    result.append('local min')
    result.append(str( dfx[0] ))
    result.append('local mxa')
    result.append(str( dfx[2] ))
    result.append('neither')
    return result 

if __name__ == '__main__':
    red_word = [6,2,5];
    for i in p22_criticalabc(red_word):
        print(i)
