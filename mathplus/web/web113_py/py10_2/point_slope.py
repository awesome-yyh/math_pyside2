# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from scipy.integrate import quad

def p10_2_point_slope(red_word):#807879,3
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    x = red_word[0]*t**3; y = red_word[1]+red_word[2]*t-t**2; slope = 1;
    #
    m = diff(y,t) / diff(x,t);
    tm = solve(m - slope);
    tmin = min(tm);
    tmax = max(tm);
    xmin = x.subs(t, tmin); ymin = y.subs(t, tmin);
    xmax = x.subs(t, tmax); ymax = y.subs(t, tmax);
    result.append(str( xmin ))
    result.append(str( ymin ))
    result.append(str( xmax ))
    result.append(str( ymax ))
    return result

def p10_2_len_exp(red_word):
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    result.append(str(red_word[2]))
    result.append(str(red_word[1]))
    result.append(r'\sqrt{e^{2\cdot t}+4\cdot t^2}')
    def f(t):
        return sqrt(exp(2*t)+4*t**2)
    s,err = quad(f,red_word[1],red_word[2])
    result.append(str(round(float(s),4)))
    return result

def p10_2_len_rt_exp(red_word):
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    x = exp(t)-t
    y = red_word[0]*exp(t/2)
    dx = diff(x); dy = diff(y);
    a = sqrt(dx**2 + dy**2)
    s = integrate(a,(t,red_word[1], red_word[2]))
    result.append(str(float(s)))
    result.append(str(simplify(s)))
    return result

def p10_2_point_slope4(red_word):#807879,4
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    x = red_word[0]*t**3; y = red_word[1]+red_word[2]*t+red_word[3]*t**2; slope = 1;
    #
    m = diff(y,t) / diff(x,t);
    tm = solve(m - slope);
    tmin = min(tm);
    tmax = max(tm);
    xmin = x.subs(t, tmin); ymin = y.subs(t, tmin);
    xmax = x.subs(t, tmax); ymax = y.subs(t, tmax);
    result.append(str( xmin ))
    result.append(str( ymin ))
    result.append(str( xmax ))
    result.append(str( ymax ))
    return result

def p10_2_s_kh_sin(red_word):
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    xi  = red_word[0]
    kxi = red_word[1]
    x = xi*(kxi*t-sin(kxi*t))
    y = xi*(1-cos(kxi*t))
    #
    dx = diff(x);
    s = integrate(dx*y,(t,0, 2*pi/kxi))
    result.append(str(simplify(s)))
    return result

def p10_2_rightmost_point(red_word):#807959,2
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    x = red_word[0]*t- red_word[1] *t**6; y = exp(t);
    #
    dxdt = diff(x)
    tx = solve(dxdt)
    xx = x.subs(t, tx[0])
    yy = y.subs(t, tx[0])
    #
    result.append(str( round(float(xx),2) ))
    result.append(str( round(float(yy),2) ))
    return result

def p10_2_3_e(red_word):#1289668,1
    result = []
    result.append('3-e')
    return result

def p10_2_dis_ab(red_word):#1289510,3
    red_word = list(map(int,red_word))
    result = []
    ##
    a = red_word[0]*2*red_word[2]*sqrt(2)
    b = red_word[0]*sqrt(2)
    #
    result.append(latex(a))
    result.append(latex(b))
    return result

def p10_2_area_texp(red_word):
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    ##
    result.append(str(red_word[1]))
    result.append('0')
    result.append(r'2\cdot \pi \cdot \left(t^2+1\right)\cdot e^t\cdot \sqrt{e^{2\cdot t}\cdot \left(t+1\right)^2\cdot \left(t^2+2\cdot t+2\right)}')
    def half_circle(t):
        return 2*pi*(t**2+1)*exp(t)*sqrt(exp(2*t)*(t+1)**2*(t**2+2*t+2))
    s,err = quad(half_circle,0,red_word[1])
    #
    result.append(str(round(float(s),4)))
    return result

def p10_2_len_sqrt(red_word):
    red_word = list(map(int,red_word))
    t = symbols('t')
    result = []
    ##
    result.append(str(red_word[1]))
    result.append(str(red_word[0]))
    result.append(r'\frac{t+2}{2\cdot t\cdot \sqrt{t+1}}')
    def a(t):
        return (t+2)/(2*t*sqrt(t+1))
    s,err = quad(a,red_word[0],red_word[1])
    #
    result.append(str(round(float(s),4)))
    return result

def p10_2_len_yin_2(red_word):#1287980,5**结果无法正常表示**
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    x = red_word[0]+red_word[1]*t**2
    y = red_word[2]+red_word[3]*t**3
    tt = [0, red_word[4]]
    #
    t0 = tt[0]; t1 = tt[1];
    dx = diff(x); dy = diff(y);
    a = sqrt(dx**2 + dy**2);
    print(a)
    dis = integrate(a, (t,t0, t1));
    #
    result.append(latex(dis))
    result.append(float(dis))
    # result.append(latex(b))
    return result

def p10_2_s_tan_st(red_word):#807879,3
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    cc = red_word[0]
    st = red_word[1]
    if st == 2:
        k = 'sqrt(3)/3'
        b = 'cc-cc/9*pi*sqrt(3)'.replace('cc',str(cc*2))
    elif st == -2:
        k = '-sqrt(3)/3'
        b = 'cc-cc/9*pi*sqrt(3)'.replace('cc',str(cc*2))
    elif st == 4:
        k = '-sqrt(3)/3'
        b = 'cc+c4/9*pi*sqrt(3)'.replace('cc',str(cc*2)).replace('c4',str(cc*4))
    elif st == -4:
        k = 'sqrt(3)/3'
        b = 'cc+c4/9*pi*sqrt(3)'.replace('cc',str(cc*2)).replace('c4',str(cc*4))
    elif st == 8:
        k = 'sqrt(3)/3'
        b = 'cc-c8/9*pi*sqrt(3)'.replace('cc',str(cc*2)).replace('c8',str(cc*8))
    elif st == -8:
        k = '-sqrt(3)/3'
        b = 'cc-c8/9*pi*sqrt(3)'.replace('cc',str(cc*2)).replace('c8',str(cc*8))

    result.append(k+'*x+'+b)
    result.append('(2n+1)pi')
    result.append('2npi')
    return result

if __name__ == '__main__':
    red_word = [4,6];
    for i in p10_2_len_sqrt(red_word):
        print(i)
