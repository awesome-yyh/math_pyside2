# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p7_4_int_3d4(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    f = (x**3+red_word[1]*x)/(x**4+red_word[2]*x**2+red_word[3])
    s = integrate(f,(x,red_word[4],red_word[0]))
    result.append(latex(simplify(s)).replace('log','ln'))
    return result

def p7_4_int_xd(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    f = x/(x**2 + red_word[1]*x + red_word[2])
    s = integrate(f, (x, red_word[3], red_word[0]))
    result.append(latex(simplify(s)).replace('log','ln'))
    return result

def p7_4_int_xd2(red_word): # 1817474, 5
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[(rw0*x + rw1)/(rw2*x^2 + rw3*x - rw4), x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    s = s.replace('rw2',str(red_word[2]))
    s = s.replace('rw3',str(red_word[3]))
    s = s.replace('rw4',str(red_word[4]))
    result.append(s)
    return result

def p7_4_int_x2d(red_word): # 1817242, 4
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = integrate((red_word[0] *x**2 + red_word[1]*x - red_word[2])/(x**3 + red_word[3] *x**2), x)
    result.append(latex(simplify(s)).replace('log','ln'))
    result.append('add |...|')
    return result

def p7_4_int_x3d(red_word): # 1816838, 4
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = 'Integrate[(rw0*x^3 + x^2 + rw1*x + rw2)/((x^2 + 1)*(x^2 + rw3)), x]'
    s = s.replace('rw0',str(red_word[0]))
    s = s.replace('rw1',str(red_word[1]))
    s = s.replace('rw2',str(red_word[2]))
    s = s.replace('rw3',str(red_word[3]))
    result.append(s)
    return result

def p7_4_int_x3d2(red_word): # 1816375, 4
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    s = integrate((x**3 + red_word[0])/ (x**2 + red_word[1]), x)
    result.append(latex(simplify(s)).replace('log','ln'))
    return result

def p7_4_int_dt2(red_word): # 1816276, 3
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    #
    s = '\\frac{rw0}{rwa}\\cdot \\left(\\ln \\left(\\left|t-rw2\\right|\\right)-\\ln \\left(\\left|rw1+t\\right|\\right)\\right)'
    s = s.replace('rw0',str(red_word[0])).replace('rw1',str(red_word[1])).replace('rw2',str(red_word[2])).replace('rwa',str(red_word[1]+red_word[2]))
    result.append(s)
    return result

def p7_4_int_t_d3(red_word): # 1816276, 3
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    f = red_word[0]/(x**3- red_word[1])
    s = integrate(f,x)
    result.append(latex(simplify(s)).replace('log','ln'))
    result.append('add |..|')
    return result

def p7_4_int_s_2d3(red_word): # 1816276, 3
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    #
    f = (red_word[0]*x**2+red_word[1]*x+red_word[2])/(x**3+red_word[3]*x)
    s = integrate(f,x)
    result.append(str(simplify(s)).replace('log','ln').replace('atan','arctan'))
    result.append('add |..|, first / then arctan')
    return result

def p7_4_int_z_2d3(red_word):
    red_word = list(map(float,red_word))
    result = []
    #
    result.append('x^2+4')
    result.append('x')
    result.append('A+B')
    result.append('C')
    result.append('4\\cdot A')
    result.append(str(int(red_word[0])))
    result.append(str(int(-red_word[1])))
    A = [[1, 1, 0],
    [0, 0, 1],
    [4, 0, 0]]
    b = [red_word[0],-red_word[1],red_word[2]]
    r=np.linalg.solve(A,b)
    result.append(str(int(r[0])))
    result.append(str(int(r[1])))
    result.append('\\ln \\left(\\left|x\\right|\\right)')
    result.append('\\ln \\left(\\left|4+x^2\\right|\\right)')
    result.append('\\operatorname{atan}\\left(\\frac{x}{2}\\right)')
    return result

if __name__ == '__main__':
    red_word = [8,7,24,8,7,24,24,-7,6,3.5];
    for i in p7_4_int_z_2d3(red_word):
        print(i)
