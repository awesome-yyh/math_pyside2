# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p28_int1(df,x0,fx0):
    x = symbols('x')
    c = fx0 - integrate(df,x).subs(x,x0)
    f = integrate(df,x)+c
    return simplify(f)

def p28_intsec(ddf,x0,fx0,xd0,fxd0):
    x = symbols('x')
    c1 = fxd0 - integrate(ddf,x).subs(x,xd0)
    df = integrate(ddf,x)+c1
    c2 = fx0 - integrate(df,x).subs(x,x0)
    f = integrate(df,x)+c2
    return simplify(f)

def p28_int2(red_word):#3804246,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**2- red_word[0]*x+ red_word[1]
    result.append(latex(integrate(f,x)) + '+C')
    return result 

def p28_intzf(red_word):#3804459,6
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = red_word[0]*x**(red_word[1]/red_word[2]) + red_word[3]*x**(-red_word[4]/red_word[5])
    result.append(latex(integrate(f,x)) + '+C')
    return result 

def p28_sqrt2(red_word):#3804286,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = x**(2/red_word[0])+x*sqrt(x)
    result.append(latex(integrate(f,x)) + '+C')
    return result 

def p28_secte(red_word):#3803468,1
    red_word = list(map(int,red_word))
    s = symbols('s')
    result = []
    #
    f = sec(s)*tan(s)- red_word[0]*exp(s)
    result.append(latex(simplify(integrate(f,s))) + '+C')
    return result 

def p28_4d3(red_word):#3804460,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (2*x**4+red_word[0]*x**3-x)/x**3
    result.append(latex(simplify(integrate(f,x))) + '+C')
    return result 

def p28_321(red_word):#3803635,3
    red_word = list(map(int,red_word))
    x,C,D = symbols('x C D')
    result = []
    #
    ddf = red_word[0]*x**3- red_word[1]*x**2 +red_word[2]*x
    df = simplify(integrate(ddf,x))+C
    f = simplify(integrate(df,x))+D
    result.append(latex(f) )
    return result 

def p28_int1_sqrt(red_word):#3804168,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    df = 1+3*sqrt(x)
    x0 = red_word[0];
    fx0 = red_word[1];
    ##
    result.append(latex(p28_int1(df,x0,fx0)))
    return result 

def p28_int1_sec(red_word):#3803314,1
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    df = sec(x)*(sec(x)+tan(x))
    x0 = pi/4;
    fx0 = - red_word[0];
    ##
    result.append(latex(p28_int1(df,x0,fx0)))
    return result 

def p28_int2_2(red_word):#3804295,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    ddf = -2+ red_word[0]*x-12*x**2
    x0 = 0;
    fx0 = red_word[1];
    dx0 = 0
    fdx0 = red_word[2];
    ##
    result.append(latex(p28_intsec(ddf,x0,fx0,dx0,fdx0)))
    return result 

def p28_int1_tan(red_word):#3803815,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    df = red_word[0]*x**3
    x0 = solve(red_word[0]*x**3+red_word[1])[0]
    fx0 = (- red_word[1]*x).subs(x,x0)
    ##
    result.append(latex(p28_int1(df,x0,fx0)))
    return result 

def p28_gmarginal(red_word):#3804543,8
    red_word = list(map(float,red_word))
    x = symbols('x')
    result = []
    #
    cp = red_word[0]-red_word[1]*x
    c = integrate(cp,x)
    result.append(latex(c))
    result.append(str(red_word[2]))
    C = red_word[2]- c.subs(x,1)
    result.append(str(C))
    f = c+C
    result.append(str( f.subs(x,100) ))
    return result 

if __name__ == '__main__':
    red_word = [ 1.92,0.004,558];
    for i in p28_gmarginal(red_word):
        print(i)
