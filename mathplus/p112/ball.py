from sympy import *
t = symbols('t')
##
v0 = 96;
h0 = 128;
acc = -64;
##
v = v0+integrate(acc,(t,0,t))
h = h0 + integrate(v,(t,0,t))
t0 = solve(v);
print('v: ', v)
print('h: ', h)
print(h.subs(t,t0[0]))
