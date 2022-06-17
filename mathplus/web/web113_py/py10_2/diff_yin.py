# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p10_2_diff_yin_d(red_word):#1288459,1
    red_word = list(map(int,red_word))
    result = []
    t = symbols('t')
    ##
    x = red_word[0]/t;  y = sqrt(t)*exp(-t);
    #
    dydx = diff(y) / diff(x);
    result.append(latex( simplify(dydx )))
    return result

if __name__ == '__main__':
    red_word = [2];
    red_word = list(map(int,red_word))
    for i in p10_2_diff_yin_d (red_word):
        print(i)


# syms t  %使d2大于0的x
# % x = t+log(t); y = t-log(t);  % 0到无穷  INFINITY
# % \frac{t-1}{t+1}
# % \frac{2\cdot t}{\left(t+1\right)^3}
# % x = t-exp(t); y = t+exp(-t); % -无穷到0
# % -\exp{-t}
# % -\frac{\exp{-t}}{\exp{t}-1}
# % x = exp(sqrt(t)); y = t-log(t^3);
# % x = 9/t;  y = sqrt(t)*exp(-t);
# % x = t*sin(t);  y = t^2+4*t; %算完改 \frac{2\cdot t+1}{\sin \left(t\right)+t\cdot \cos \left(t\right)}
# % x = cos(2*t); y = cos(t);
# % \frac{1}{4\cdot \cos \left(t\right)}
# % -\frac{1}{16\cdot \cos \left(t\right)^3}
# % || pi/2 3/2*pi(看题)
# % x = 5*sin(t); y = 6*cos(t); %区间：pi/2 3*pi/2 
# % x = t^3-12*t; y = t^2-1; % 看一下第二个的分母就知道
# % x = 7+t^2; y = t^2 + t^3;  %0 到 无穷 INFINITY
# % x = 2*t^2; y = 4*exp(t);
# % x = t^4; y = t^3-6*t;
# %%
# dydx = diff(y) / diff(x);
# pretty(simplify(dydx))
# d2 = diff(dydx)/diff(x);
# pretty(simplify(d2))