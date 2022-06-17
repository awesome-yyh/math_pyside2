# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_hydrostatic_swimming(red_word):#1817264,4
    red_word = list(map(int,red_word))
    result = []
    x,t = symbols('x t')
    ##
    wide =    red_word[0];
    longs =   red_word[1];
    shallow = red_word[2];
    deep =    red_word[3];
    ro = 62.5;
    #
    delta = ro;
    f_shallow = integrate(delta*x*wide,(x, 0, shallow));
    result.append(str(round(float(f_shallow),1)))
    #
    f_deep = integrate(delta*x*wide, (x,0, deep));
    result.append(str(round(float(f_deep),1)))
    #
    f_side = integrate(delta*x*longs,(x, 0, shallow)) + integrate(delta*x*longs*(deep-x)/(deep-shallow),(x,shallow,deep));
    result.append(str(round(float(f_side),1)))
    #
    f_bottom = integrate(delta*x*wide*(longs**2+(deep-shallow)**2)**(1/2)/(deep-shallow), (x,shallow, deep));
    result.append(str(round(float(f_bottom),1)))
    return result

if __name__ == '__main__':
    red_word = [10,20,4,9];
    red_word = list(map(int,red_word))
    for i in p8_3_hydrostatic_swimming(red_word):
        print(i)
