# 返回元素为字符串的list
# 参数是[100,800]的list
from sympy import *
import numpy as np
from math import ceil

def p7_7_TMS_f_plus_none():
    x = symbols('x')
    red_word = 0;
    #
    y = exp(x**2);x0=0;x1=2;n=5;ee=0.00001;flag='e';
    return TMS_f_plus(y,x0,x1,n,ee,red_word,flag)

def p7_7_LRTM_xexp(red_word):
    red_word = list(map(int,red_word))
    x = symbols('x')
    #
    y = red_word[0]*x*exp(x); x0 = 0; x1 = 1; n = 5;
    return LRTM(y,x0,x1,n/2)

def p7_7_TMS_f_plus_sin(red_word):
    red_word = list(map(float,red_word))
    x = symbols('x')
    #
    y = red_word[0]*sin(x);x0=0;x1=pi;n=10;ee=0.00001;flag='sin';#%这个s最后可能减1，同时下面参数也要改
    return TMS_f_plus(y,x0,x1,n,ee,red_word,flag)



    ##
def TMS_f_plus(y,x0,x1,n,ee,red_word,flag):
    result = []
    x = symbols('x')
    #
    ## 求绝对误差时的参数 S是四阶导的最大值,M是二阶导的
    dy2 = diff(diff(y))
    dy4 = diff(diff(dy2))
    if flag == 'sin':  #\三角函数的上届取1
        # disp('#求绝对误差和n时，三角函数,kt km看dy2的各项绝对值的系数之和,ks看dy4的')
        kt = red_word[0];
        ks = red_word[0];
        km = kt;
    elif flag == 's':
        # disp('#求绝对误差和n时，三角函数,kt km看dy2的各项绝对值的系数之和,ks看dy4的')
        kt = 27+0;
        ks = 27+0+0;
        km = kt;
    elif flag == 'e':
        kt = max(dy2.subs(x,x1), dy2.subs(x,x0));
        km = kt;
        ks = max(dy4.subs(x,x1), dy4.subs(x,x0));
    ## 公共部分
    delta = (x1-x0)/n;
    inte = integrate(y, (x,x0, x1));
    ## Trapezoidal Rule
    xt = np.arange(x0,x1+delta,delta)
    xtp = np.arange(2,len(xt),1)
    sxtp = 0
    for i in xtp:
        sxtp += y.subs(x,xt[i-1])
    tn = delta * 1/2 * (y.subs(x,x0) + 2* sxtp+ y.subs(x,x1));
    te = inte - tn;
    ## Midpoint Rule
    xm = np.arange(x0+delta/2, x1+delta/2,delta)
    sxm = 0
    for i in xm:
        sxm += y.subs(x,i)
    mn = delta * sxm;
    me = inte - mn;
    ## Simpsons Rule
    xs = np.arange(x0,x1+delta,delta)
    lens = len(xs);
    f4 = np.arange(2,lens+1,2)
    f2 = np.arange(3,lens,2)
    sxsf4 = 0
    for i in f4:
        sxsf4 +=  y.subs(x,xs[i-1])
    sxsf2 = 0
    for i in f2:
        sxsf2 += y.subs(x,xs[i-1])
    sn = delta * 1/3 * (y.subs(x,xs[0]) + 4*sxsf4 + 2*sxsf2 + y.subs(x,xs[lens-1]));
    se = inte - sn;
    #
    ## 求绝对误差
    absme = km * (x1-x0)**3 / (24*n**2);
    absse = ks * (x1-x0)**5 / (180*n**4);
    abste = kt * (x1-x0)**3 / (12*n**2);
    ## 求n
    nt = sqrt(kt*(x1-x0)**3 / 12/ee); nt = ceil(nt);
    nm = sqrt(km*(x1-x0)**3 / 24/ee); nm = ceil(nm);
    ns = (ks*(x1-x0)**5 / 180/ee)**(1/4); ns = ceil(ns)+1;
    result.append(str(round(float(tn),6)))
    result.append(str(round(float(mn),6)))
    result.append(str(round(float(sn),6)))

    result.append(str(round(float(te),6)))
    result.append(str(round(float(me),6)))
    result.append(str(round(float(se),6)))

    result.append(str(round(float(abste),6)))
    result.append(str(round(float(absme),6)))
    result.append(str(round(float(absse),6)))

    result.append(str(round(int(nt),6)))
    result.append(str(round(int(nm),6)))
    result.append(str(round(int(ns),6)))

    return result

def LRTM(y,x0,x1,n):
    result = []
    tns = []
    tes = []
    mns = []
    mes = []
    lns = []
    les = []
    rns = []
    res = []
    x = symbols('x')
    #
    for i in range(3):
        n = n*2
        ## 公共部分
        delta = (x1-x0)/n;
        inte = integrate(y, (x,x0, x1));
        ## Trapezoidal Rule
        xt = np.arange(x0,x1+delta,delta)
        xtp = np.arange(2,len(xt),1)
        sxtp = 0
        for i in xtp:
            sxtp += y.subs(x,xt[i-1])
        tn = delta * 1/2 * (y.subs(x,x0) + 2* sxtp+ y.subs(x,x1));
        te = inte - tn;
        tns.append(tn)
        tes.append(te)
        ## Midpoint Rule
        xm = np.arange(x0+delta/2, x1+delta/2,delta)
        sxm = 0
        for i in xm:
            sxm += y.subs(x,i)
        mn = delta * sxm;
        me = inte - mn;
        mns.append(mn)
        mes.append(me)
        ## left rule
        xl = np.arange(x0,x1,delta)
        sxl = 0
        for i in xl:
            sxl += y.subs(x,i)
        ln = delta*sxl
        le = inte - ln
        lns.append(ln)
        les.append(le)
        ## right rule
        xr = np.arange(x0+delta,x1+delta,delta)
        sxr = 0
        for i in xr:
            sxr += y.subs(x,i)
        rn = delta*sxr
        re = inte - rn
        rns.append(rn)
        res.append(re)
        ##
    for i in range(3):
        result.append(str(round(float(lns[i]),6)))
        result.append(str(round(float(rns[i]),6)))
        result.append(str(round(float(tns[i]),6)))
        result.append(str(round(float(mns[i]),6)))
    for i in range(3):
        result.append(str(round(float(les[i]),6)))
        result.append(str(round(float(res[i]),6)))
        result.append(str(round(float(tes[i]),6)))
        result.append(str(round(float(mes[i]),6)))
    result.append('2')
    result.append('4')
    return result
# if __name__ == '__main__':
#     red_word = [13]; #1816261
#     for i in p7_7_TMS_f_plus_sin(red_word):
#         print(i)

if __name__ == '__main__':
    red_word = [10,1.8];
    for i in p7_7_s_mnexp(red_word):
        print(i)