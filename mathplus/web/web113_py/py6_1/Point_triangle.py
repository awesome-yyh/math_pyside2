# 返回元素为字符串的list
# 参数是[100,800]的list
import numpy as np

def p6_2_midpoint():
    result = []
    #
    ## 参数
    p1 = [0, 0];
    p2 = [5, 4];
    p3 = [-1,8];
    ##
    x1 = p1[0]; y1 = p1[1];
    x2 = p2[0]; y2 = p2[1];
    x3 = p3[0]; y3 = p3[1];
    ## 计算
    a = ((x1-x2)**2 + (y1-y2)**2)**(1/2);
    b = ((x1-x3)**2 + (y1-y3)**2)**(1/2);
    c = ((x3-x2)**2 + (y3-y2)**2)**(1/2);
    s = 1/2 * (a+b+c);
    S = (s*(s-a)*(s-b)*(s-c))**(1/2);
    #
    result.append(str(abs(S)))
    return result

if __name__ == '__main__':
    for i in p6_2_midpoint():
        print(i)
