from sympy import *
import numpy as np

n = symbols('n')
#

# y = (sin(13*n))**2 / n**2; yy = 1/n**2;  nn = 10; #因为(sin())**2 <= 1
y = 1/(n**4+2); yy = 1/n**4; nn = 6;
# y = 3/sqrt(n**6+3); yy = 3/sqrt(n**6);nn = 10; ##y2就算把sqrt里面的常数去掉
# # y = 4*n/((n+1)*3**n); ##这个用sn_err求
# # y = /(1+2**n); yy = 18/2**n;##这个用sum_err_pro求
##
sn = symsum(y,1,nn);
fprintf('sn从1到n #.6f\n',sn);
snsn = int(yy,nn,inf);
fprintf('误差 #.6f\n',snsn)