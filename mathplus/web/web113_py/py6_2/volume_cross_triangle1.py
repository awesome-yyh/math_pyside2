# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
import pyperclip

x = symbols('x')
#底
y1 = 1-4*x**2;
y2 = 0;
#高  垂直于x轴的横截面是高等于底的等腰三角形
h = y1;
b = y1;
## 计算
#(绕y=d，轴写x的范围，pi*（y-d）^2的值)
#(绕x=d，轴写y的范围，pi*（x-d）^2的值)
xx = solve(y1-y2);
x1 = xx[0]; x2 = xx[1];
a = 1/2 * b * h;
v = integrate(a, (x,x1, x2));
print(v)
pyperclip.copy(str(v))
print('已复制')