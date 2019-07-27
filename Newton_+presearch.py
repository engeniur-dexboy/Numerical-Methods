print('1) Find the root of y= x^3 - 3.5x +1.2 by Newton\'s Method')

from numpy import *

def f(x): return x**3 -3.5*x +1.2
def dfdx(x): return 3*x**2 -3.5

a=eval(input('\nEnter value of lowerbound initial guess:'))
b=eval(input('Enter value of upperbound initial guess:'))

n=1000
inter=(b-a)/n

print('\nPre-search values:')
x1=0
for i in arange(a,b,inter):
    ya=f(i)
    yb=f(i+inter)
    if ya*yb<=0:
        x1=i
        print('x1o= {:1.6f}'.format(x1))
        break

for i in arange(x1+inter,b,inter):
    ya=f(i)
    yb=f(i+inter)
    if ya*yb<=0:
        x2=i
        print('x2o= {:1.6f}'.format(x2))
        break

for i in arange(x2+inter,b,inter):
    ya=f(i)
    yb=f(i+inter)
    if ya*yb<=0:
        x3=i
        print('x3o= {:1.6f}'.format(x3))
        break

print('\nBy Newton-Raphson:')
x=x1    
for n in range(1,100):
    if dfdx(x)==0:
        print('x1 not determined')
    else:
        xn=x-f(x)/dfdx(x)
        if abs(xn-x)<=0.000001:
            print('x1= {:1.6f}'.format(xn))
            break
    x=xn

x=x2    
for n in range(1,100):
    if dfdx(x)==0:
        print('x2 not determined')
    else:
        xn=x-f(x)/dfdx(x)
        if abs(xn-x)<=0.000001:
            print('x2= {:1.6f}'.format(xn))
            break
    x=xn

x=x3    
for n in range(1,100):
    if dfdx(x)==0:
        print('x3 not determined')
    else:
        xn=x-f(x)/dfdx(x)
        if abs(xn-x)<=0.000001:
            print('x3= {:1.6f}'.format(xn))
            break
    x=xn

input('\nPress return to exit')
