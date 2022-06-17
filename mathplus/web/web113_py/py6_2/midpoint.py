# 返回元素为字符串的list
# 参数是[100,800]的list
import numpy as np

def p6_2_midpoint(red_word):
    red_word = list(map(float,red_word))
    result = []
    ##
    y = [0]+red_word+[0]
    x = np.arange(0,15+1.5,1.5)
    n = 5
    ##
    k = (len(y)-1)/n;
    xs = np.arange(2,len(y)-1+k,k)
    s = 0
    for i in xs:
        s += 3*y[int(i)-1]

    result.append(str(abs(s)))
    return result

def p6_2_midpoint_min(red_word):
    red_word = list(map(float,red_word))
    result = []
    ##
    x = np.arange(0,red_word[0]+red_word[1],red_word[1])
    y = red_word[2::2]
    yl = y[0::2]
    yr = y[1::2]
    y = yl+yr
    n = 5
    ##
    k = (len(y)-1)/n;
    xs = np.arange(2,len(y)-1+k,k)
    s = 0
    for i in xs:
        s += red_word[0]/5*y[int(i)-1]

    result.append(str(abs(s)))
    return result

if __name__ == '__main__':
    red_word = [5,0.5,0.69,3,0.53,0.5,0.65,3.5,0.56,1,0.63,4,0.52,1.5,0.62,4.5,0.50,2,0.58,5,0.48,2.5,0.59]
    for i in p6_2_midpoint_min(red_word):
        print(i)

