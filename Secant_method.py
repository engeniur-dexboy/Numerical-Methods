print('Find the smallest positive value of x in xsin(x)=cos(x/3)')
print('SECANT METHOD')
print('Initial guesses: x0=0 and x1=1')

from math import sin,cos

def f(x): return x*sin(x)-cos(x/3)
x0=0
x1=1
print('  0 : x={:1.3f}'.format(x0))
print('  1 : x={:1.3f}'.format(x1))

for n in range(2,100):
    x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
    print('{:3d}'.format(n),': x={:1.3f}'.format(x2))
    if abs(x2-x1)<=0.001:
        x =x2
        print('root= {:1.3f}'.format(x))
        input('\nPress return to exit')
        break
    x0=x1
    x1=x2
    
    

