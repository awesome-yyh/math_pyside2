# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p6_1_none():
    result = []
    x = symbols('x')
    ##
    # y1 = x+2; y2 = 15-1*x**2; xxx = [-1,2]
    # y1 = 2*cos(2*x); y2 = 2-2*cos(2*x); xxx = solve(y1-y2);print(xxx); xxx = [1/2*pi, 1/6*pi]; #有的分段
    # y1 = 7*cos(2*x);y2=7*sin(4*x);xxx = solve(y1-y2);print(xxx)
    # y1 = x**2; y2 = sqrt(x);xxx = solve(y1-y2);
    # y1 = tan(2*x); y2 = 2*sin(2*x);xxx = [0, pi/6];print('结果乘以2')
    # y1 = 3/2*sin(pi*x/4);y2 = 3/4*x;#xxx = solve(y1-y2);print(xxx)
    # xxx = [0, 4/2];print('结果*2')#xxx的第二个点要画图(打开画图语句)，看第二个点横坐标，都是...5
    # Plot[{2/1*Sin[Pi*x/3], 4/3*x}, {x, 0, 5}]
    # y1 = 4+1*sqrt(x); y2 = (12+x)/3; xxx = solve(y1-y2);
    # y1 = (13-x**2)/6; y2 = 2*x; xxx = solve(y1-y2);
    # y1 = x**2-1*x; y2 = 3*x-x**2; xxx = solve(y1-y2);
    y1 = x**2-4*x; y2 = 5*x+0; xxx = solve(y1-y2);
    # y1 = 1*x**2; y2 = 4+0*x+2*x**2; xxx = solve(y1-y2);
    # y1 = x**2;y2=6/(x**2+5); xxx = solve(y1-y2);xxx=[xxx[0],xxx[1]]
    # y1 = 5*x; y2 = x**2 - 6; xxx = solve(y1-y2); xxx_ = solve(-y1-y2); xxx = xxx+xxx_
    # y1 = 19-1*x**2; y2 = 1*x**2-13;xxx = solve(y1-y2);print(xxx);#xxx = [1, 3]; #有的分段
    return p6_1_area_2(y1,y2,xxx,result)

def p6_1_s_x2(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = red_word[0]* x**2+red_word[1]*x; y2 = red_word[2]*x
    xxx = solve(y1-y2)
    s = integrate(y1-y2, (x,xxx[0],xxx[1]));
    result.append(str(abs(s)))
    return result

def p6_1_t_x3(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = x**3- red_word[0]*x; y2 = red_word[1]*x
    xxx = solve(y1-y2)
    s = integrate(y1-y2, (x,xxx[0],xxx[1]));
    result.append(str(abs(s)))
    return result

def p6_1_t_sin_plot(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = red_word[0]/red_word[1]*sin(pi*x/red_word[2])
    y2 = red_word[3]/red_word[4]*x
    ss = []
    for i in range(10):
        xxx = [0, (i+1)/2]
        s = integrate(y1-y2, (x,xxx[0],xxx[1]));
        ss.append(str(abs(s)*2))
    f = min(ss,key=len)
    result.append(latex(f))
    return result

def p6_1_t_x2kh(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = (red_word[1] -x**2)/red_word[0]; y2 = red_word[2]*x
    xxx = solve(y1-y2)
    s = integrate(y1-y2, (x,xxx[0],xxx[1]));
    result.append(str(abs(s)))
    return result

def p6_1_t_x2x2(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = red_word[0]-x**2;y2=x**2-red_word[1]
    xxx = solve(y1-y2)
    s = integrate(y1-y2, (x,xxx[0],xxx[1]));
    result.append(str(abs(s)))
    return result

def p6_1_cos__cos(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = red_word[0]*cos(x);y2=red_word[1]-red_word[2]*cos(x)
    xxx = [0,2*pi]
    s = integrate(y1-y2, (x,xxx[0],xxx[1]));
    result.append(latex(abs(s)))
    return result

def p6_1_t_x2x(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = x**2-red_word[0]*x;y2=red_word[1]*x+red_word[2]
    xxx = solve(y1-y2);
    s = integrate(y1-y2, (x,xxx[0],xxx[1]));
    result.append(str(abs(s)))
    return result

def p6_1_t_2d(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = x**2;y2=red_word[0]/(x**2+red_word[1]); xxx = solve(y1-y2);
    s = integrate(y1-y2, (x,xxx[0],xxx[1]));
    result.append(str(abs(round(float(s),3))))
    return result

def p6_1_t_2(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x') 
    ##
    y1 = red_word[0]*x**2;y2=red_word[1]+red_word[2]*x**2;xxx = solve(y1-y2);
    return p6_1_area_2(y1,y2,xxx,result)

def p6_1_t_cos_sin(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    y1 = red_word[0]*cos(red_word[1]*x)
    y2 = red_word[2]*sin(red_word[3]*x)
    xxx = [pi/(3*red_word[3]), pi/red_word[3]]
    s1 = integrate(y1-y2, (x,xxx[0], xxx[1]) )
    s = abs(s1*2)
    result.append(str(round(float(s),3)))
    return result

def p6_1_t_sqrt(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    y1 = sqrt(x); y2 = red_word[0]/red_word[1]*x;xxx = solve(y1-y2);
    s1 = integrate(y1-y2, (x,int(xxx[0]), int(xxx[1])))
    s2 = integrate(y1-y2, (x,int(xxx[1]), int(red_word[2])))
    s = abs(s1)+abs(s2)
    result.append(str(float(s)))
    return result

def p6_1_t_area_2(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    y1 = red_word[0]/x; y2 = red_word[1]/x**2;
    xxx = solve(y1-y2); xxx = [xxx[0], red_word[2]];
    s = integrate(y1-y2, (x,int(xxx[0]), int(xxx[1])));
    result.append(latex(s).replace('log','ln'))
    return result

def int_t_abs(red_word):
    # red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    s = integrate(sqrt((2*x+3)-x),(x,4,3))
    result.append(str(s))
    return result

def p6_1_s_area_2(red_word):
    red_word = list(map(int,red_word))
    result = []
    x = symbols('x')
    ##
    y1 = x**3-red_word[0]*x; y2 = x**2;xxx = solve(y1-y2);
    return p6_1_area_2(y1,y2,xxx,result)

def p6_1_people(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    ##
    y1 = red_word[0] * exp(red_word[1]*x); y2 = red_word[2] * exp(red_word[3]*x);
    result.append('select --> increase')
    s = integrate(y1-y2, (x,0, 10));
    result.append(str(round(float(s))))
    return result

def p6_1_a_b(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    ##
    y1 = red_word[0]*x-x**2; y2 = red_word[1]*x;xxx = solve(y1-y2);
    return p6_1_area_2(y1,y2,xxx,result)

def p6_1_area_2(y1,y2,xxx,result):
    x = symbols('x')
    ##
    if len(xxx) == 3:
        x1 = xxx[0]; x2 = xxx[1]; x3 = xxx[2];
        s = integrate(y1-y2, (x,x1, x2)) + integrate(y2-y1,(x,x2,x3));
    elif len(xxx) == 2:
        x1 = xxx[0]; x2 = xxx[1];
        s = integrate(y1-y2, (x,x1, x2));
    elif len(xxx) == 4:
        x2 = xxx[1]; x3 = xxx[2];
        s = integrate(abs(y1)-y2, (x,x3, x2));
    ##
    result.append(str(abs(s)))
    return result

if __name__ == '__main__':
    red_word = [1, 1, 4, 1, 2];
    for i in p6_1_t_sin_plot(red_word):
    # for i in p6_1_none():
        print(i)
