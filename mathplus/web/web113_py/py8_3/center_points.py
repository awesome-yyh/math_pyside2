# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_center_points_none():
    m = [4,10,15]
    xy = [-4,3,4,-1,3,4]
    return p8_3_center_points(m,xy)

def p8_3_center_points_f11(red_word):
    red_word = list(map(float,red_word))
    m = [red_word[0], red_word[1], red_word[2]]
    xy = [-1, 1, 2, -1, 3, 2];
    return p8_3_center_points(m,xy)

def p8_3_center_points_x_axis(red_word):#806453,3
    red_word = list(map(float,red_word))
    m = red_word;
    xy = [-2, 0, 3, 0, 7, 0];
    return p8_3_center_points(m,xy)

def p8_3_s_center(red_word):#806453,3
    red_word = list(map(float,red_word))
    m = red_word[0:3]
    xy = red_word[3:]
    return p8_3_center_points(m,xy)

def p8_3_center_points(m,xy):
    result = []
    ##
    if len(xy) == 6:
        x = [xy[0],xy[2],xy[4]];
        y = [xy[1],xy[3],xy[5]];
    elif len(xy) == 8:
        x = [xy[0],xy[2],xy[4],xy[6]];
        y = [xy[1],xy[3],xy[5],xy[7]];
    else:
        print('writing error?')

    M = sum(m);
    Mx = 0
    for i in range(0,len(m)):
        Mx += m[i]*y[i]

    My = 0
    for i in range(0,len(m)):
        My += m[i]*x[i]

    xb = My / M;
    yb = Mx / M;

    result.append(str(Mx))
    result.append(str(My))
    result.append(str(xb))
    result.append(str(yb))
    return result

# if __name__ == '__main__':
#     red_word = [20,50,25]; #806453,3
#     for i in p8_3_center_points_x_axis(red_word):
#         print(i)

if __name__ == '__main__':
    red_word = [2, 9, 15, -2, 1, 4, -1, 3, 4]; #806471,12
    for i in p8_3_s_center(red_word):
        print(i)

# if __name__ == '__main__':
#     for i in p8_3_center_points_none():
#         print(i)

        