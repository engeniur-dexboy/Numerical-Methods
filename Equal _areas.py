print('Find horizontal line that bisects the curve y=x^3-3.5x+1.2')
print('into two equal areas')

from numpy import *

crit=-((3.5/3)**.5)
relmax=crit**3-3.5*crit+1.2

def f(x,yp): return x**3 -3.5*x +1.2 -yp
def dfdx(x): return 3*x**2 -3.5
    
def roots(yp):
    a=-3
    b=3

    n=1000
    inter=(b-a)/n

    for i in arange(a,b,inter):
        ya=f(i,yp)
        yb=f(i+inter,yp)
        if ya*yb<=0:
            x1=i
            break

    for i in arange(x1+inter,b,inter):
        ya=f(i,yp)
        yb=f(i+inter,yp)
        if ya*yb<=0:
            x2=i
            break

    for i in arange(x2+inter,b,inter):
        ya=f(i,yp)
        yb=f(i+inter,yp)
        if ya*yb<=0:
            x3=i
            break

    x=x1    
    for n in range(1,100):
        if dfdx(x)==0:
            print('x1 not determined')
        else:
            xn=x-f(x,yp)/dfdx(x)
            if abs(xn-x)<=0.001:
                x1=xn
                break
        x=xn

    x=x2    
    for n in range(1,100):
        if dfdx(x)==0:
            print('x2 not determined')
        else:
            xn=x-f(x,yp)/dfdx(x)
            if abs(xn-x)<=0.001:
                x2=xn
                break
        x=xn

    x=x3    
    for n in range(1,100):
        if dfdx(x)==0:
            print('x3 not determined')
        else:
            xn=x-f(x,yp)/dfdx(x)
            if abs(xn-x)<=0.001:
                x3=xn
                break
        x=xn

    return ([x1,x2,x3])

for yp in arange (1,relmax,0.001):
    xi=roots(yp)
    x1=xi[0]
    x2=xi[1]
    x3=xi[2]
    
    h1=(x2-x1)/3
    h2=(x3-x2)/3
    a1=3*h1/8*(f(x1,yp)+3*f(x1+h1,yp)+3*f(x1+2*h1,yp)+f(x2,yp))
    a2=-3*h2/8*(f(x2,yp)+3*f(x2+h2,yp)+3*f(x2+2*h1,yp)+f(x3,yp))
    if abs(a1-a2)<=0.001:
        y=yp
        print('\na1= {:1.3f}'.format(a1),'and a2= {:1.3f}'.format(a2))
        print('y= yp= {:1.3f}'.format(y))
        print('\nx1= {:1.3f}'.format(x1))
        print('x2= {:1.3f}'.format(x2))
        print('x3= {:1.3f}'.format(x3))
        break
    
import matplotlib.pyplot as plt
x=linspace(-2.5,2,400)
y1=x**3-3.5*x+1.2
y2=1.2*x/x
plt.plot(x,y2,'b')
plt.plot(x,y1,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('TWO EQUAL AREAS')
plt.show()

input('\nPress return to exit')
