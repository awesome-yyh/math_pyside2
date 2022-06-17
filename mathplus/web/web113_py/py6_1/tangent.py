# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *

def p6_1_tangent(red_word):
    red_word = list(map(float,red_word))
    result = []
    x = symbols('x')
    y1 = red_word[0]*x**2;
    x0 = red_word[1];
    ##
    k = diff(y1).subs(x,x0);
    y2 = k*(x-x0)+y1.subs(x,x0);
    y3 = 0;
    ## 计算
    x12 = solve(y1-y2);
    x12 = x12[0];
    x13 = solve(y1-y3);
    x13 = x13[0];
    x23 = solve(y2-y3);
    x23 = x23[0];
    xxx = [x12, x13, x23];
    xmax = max(xxx);
    if xmax == x12:
        s = integrate(y3-y2, (x,x23,x13)) + integrate(y1-y2, (x,x13,x12));
    elif xmax == x13:
        s = integrate(y2-y3, (x,x23,x12)) + integrate(y1-y3, (x,x12,x13));
    else:
        s = integrate(y1-y3, (x,x13,x12)) + integrate(y2-y3, (x,x12,x23));

    result.append(str(abs(s)))
    return result

if __name__ == '__main__':
    red_word = [3,3,27];
    for i in p6_1_tangent(red_word):
        print(i)

