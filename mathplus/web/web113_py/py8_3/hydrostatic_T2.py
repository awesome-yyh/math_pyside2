# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np

def p8_3_s_T2(red_word):
	red_word = list(map(int,red_word))
	x, H, l1p = symbols('x H l1p') 
	result = []
	##
	h =  red_word[0]; #高
	l1 = red_word[1]; #上底边,
	l2 = red_word[2];#下底边,
	d =  red_word[3]; #水距离上面的距离
	#
	ro = 1000; g = 9.8;
	delta = ro * g;
	# delta = 62.5;
	## 计算 side
	H = solve(H/(H-h) - l1/l2, H)[0];
	l1p = solve(H/(H-d) - l1/l1p, l1p)[0]; 
	l2p = l2;
	hp = h-d;
	dH = l1p * hp / (l1p-l2p); #补为三角形时的高
	w = l1p/dH*x; #小长条的宽
	F_side = integrate(delta * (dH - x) * w,(x, dH-hp, dH));
    #
	result.append(str(round(float(F_side),2)))
	return result

if __name__ == '__main__':
    red_word = [29,40,24,5];
    red_word = list(map(int,red_word))
    for i in p8_3_s_T2(red_word):
        print(i)
