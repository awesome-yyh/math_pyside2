from sympy import *
x, n = symbols('x n')
# y = (x-2)**n / (n*(-5)**n);
# y = (-x)**n/3**(2*n);
# y = x**n/n;
# y = (7*x-6)**n/n**5;
# y = (-1)**(n-1)*x**(3*n+2)/n;
# y = factorial(n)**2*x**n/factorial(2*n);
# y = (x-3)**n/(n**2+2);
# y = (3*x+4)**n/n**2;
y = n**2*(x-7)**n/2**n; # ()
## 
t = simplify(y.subs(n, n+1) / y.subs(n, n));
tt = limit(t, n, oo);
tx1 = solve(tt+1);
tx2 = solve(tt-1);
tx = [tx1, tx2];
tx1 = min(tx)[0]; tx2 = max(tx)[0];
r = (tx2-tx1)/2;
##
print(r, tx1, tx2)
print('R = %g, %g, %g' % (r, tx1,tx2))