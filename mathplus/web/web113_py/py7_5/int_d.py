# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_5_int_d(red_word):#1817208
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[(x - rw0)/(x^2 - rw1*x + rw2), x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    s = s.replace('rw2',str(red_word[2]))
    result.append(s)
    return result

def p7_5_int_sinsqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    #
    s = r'rw0\cdot \left(-\frac{2\cdot \sqrt{a\cdot t}\cdot \cos \left(\sqrt{a\cdot t}\right)}{a}+\frac{2\cdot \sin \left(\sqrt{a\cdot t}\right)}{a}\right)+C'
    s = s.replace('rw0',str(red_word[0]))
    result.append(s)
    return result

def p7_5_int_abs(red_word):#1817026,3
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[Abs[x^2 - rw2*x], {x, -rw1, rw0}]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    s = s.replace('rw2',str(red_word[2]))
    result.append(s)
    return result

def p7_5_int_dx4a(red_word):#1817549,2
    red_word = list(map(int,red_word))
    result = []
    #
    s = 'Simplify[TrigToExp[Integrate[rw0*x/(x^4 - a^rw1), x]]]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

def p7_5_int_dsqrt(red_word):#1816415,2
    red_word = list(map(int,red_word))
    result = []
    #
    s = 'Integrate[rw0*x^3/Sqrt[rw1 + x^2], x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

def p7_5_int_dsqrtlog(red_word):#1817377,2
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    f = red_word[0]*log(x)/(x*sqrt(red_word[1]+(log(x)**2)))
    s = integrate(f,x)
    result.append(latex(simplify(s)).replace('log','ln'))
    return result

def p7_5_int_sin2(red_word):#1817512,2
    red_word = list(map(int,red_word))
    result = []
    #
    s = 'Integrate[(rw0*x + rw1*Sin[x])^2, x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

def p7_5_int_dx4(red_word):#1817269,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    f = (red_word[0]*x)/(x**4+x**2+red_word[1])
    s = integrate(f,x)
    result.append(latex(simplify(s)))
    return result

def p7_5_int_x2d2(red_word):#1817197,4
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    s = integrate((red_word[0]*x**2- red_word[1])/(x**2-red_word[2]*x- red_word[3]) ,x)
    result.append(latex(simplify(s)).replace('log','ln'))
    result.append('///+abs')
    return result

def p7_5_int_dxx2(red_word):#1817348,2
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    s = integrate(1/((x- red_word[0])*(x**2+red_word[1])))
    result.append(latex(simplify(s)).replace('log','ln'))
    result.append('///+abs')
    return result

def p7_5_dint_td2(red_word):#1816568,3
    red_word = list(map(int,red_word))
    x = symbols('x')
    result = []
    #
    s = integrate(red_word[1]*x/(x- red_word[2])**2,(x,0,red_word[0]))
    result.append(latex(simplify(s)).replace('log','ln'))
    return result

def p7_5_int_cos(red_word):#1816226,2
    red_word = list(map(int,red_word))
    result = []
    #
    s = 'Integrate[Cos[x]*(rw0 + rw1*Sin[x]^2), x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

def p7_5_int_expsqrt(red_word):#1817123,2
    red_word = list(map(int,red_word))
    result = []
    #
    s = 'Integrate[rw0*Exp[x]*Sqrt[rw1 + Exp[x]], x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    result.append(s)
    return result

def p7_5_int_cc3sin(red_word):#1817123,2
    red_word = list(map(int,red_word))
    result = []
    #
    s = r'\frac{rw0}{12}\cdot \left(9\cdot \sin \left(\sin \left(x\right)\right)+\sin \left(3\cdot \sin \left(x\right)\right)\right)'
    s = s.replace('rw0',str(red_word[0]))
    result.append(s)
    return result

if __name__ == '__main__':
    red_word = [4]; #
    for i in p7_5_int_dsqrtlog(red_word):
        print(i)