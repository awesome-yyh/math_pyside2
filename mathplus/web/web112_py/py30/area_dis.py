# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p30_right(y,x0,x1,n):
    x = symbols('x')
    ## comm
    delta = (x1-x0)/n;
    inte = integrate(y, (x,x0, x1));
    ly = lambdify(x,y)
    ## R Rule
    xr = np.linspace(x0+delta, x1, n)
    rn = delta * sum(ly(xr));
    re = inte - rn;
    return [rn, re]

def p30_left(y,x0,x1,n):#
    x = symbols('x')
    ## comm
    delta = (x1-x0)/n;
    inte = integrate(y, (x,x0, x1));
    ly = lambdify(x,y)
    ## L Rule
    xl = np.linspace(x0, x1-delta, n)
    ln = delta * sum(list(ly(xl)));
    le = inte - ln;
    return [ln, le]

def p30_mid(y,x0,x1,n):#
    x = symbols('x')
    ## comm
    delta = (x1-x0)/n;
    inte = integrate(y, (x,x0, x1));
    ly = lambdify(x,y)
    # middle
    xm = np.linspace(x0+delta/2, x1-delta/2, n)
    mn = delta * sum(ly(xm));
    me = inte - mn;
    return [mn, me]

def p30_r36(red_word):#3804037,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]+red_word[1]*x**2
    x0 = -1; x1 = 2
    R3 = p30_right(f,x0,x1,3)[0]
    result.append(str(R3))
    R6 = p30_right(f,x0,x1,6)[0]
    result.append(str(R6))
    result.append('right')
    result.append('right')
    L3 = p30_left(f,x0,x1,3)[0]
    result.append(str(L3))
    L6 = p30_left(f,x0,x1,6)[0]
    result.append(str(L6))
    result.append('left-')
    result.append('left-')
    M3 = p30_mid(f,x0,x1,3)[0]
    result.append(str(M3))
    M6 = p30_mid(f,x0,x1,6)[0]
    result.append(str(M6))
    result.append('middle')
    result.append('middle')
    result.append('m6')
    return result 

def p30_runner(red_word):#3803873,7
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    #
    result.append('L6')
    result.append('R6')
    result.append('0.5')
    result.append(str( red_word[0] ))
    result.append(str( red_word[1] ))
    result.append(str( red_word[2] ))
    result.append(str( red_word[3] ))
    result.append(str( red_word[4] ))
    result.append(str( red_word[5] ))
    result.append(str( sum(red_word[0:6])/2 ))

    result.append(str( red_word[1] ))
    result.append(str( red_word[2] ))
    result.append(str( red_word[3] ))
    result.append(str( red_word[4] ))
    result.append(str( red_word[5] ))
    result.append(str( red_word[6] ))
    result.append(str( sum(red_word[1:7])/2 ))
    return result 

if __name__ == '__main__':
    red_word = [0,6.2,10.8,14.9,18.1,19.4,20.2]
    for i in p30_runner(red_word):
        print(i)
