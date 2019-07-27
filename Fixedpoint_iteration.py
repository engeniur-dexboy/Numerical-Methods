print('Find the smallest positive value of x in xsin(x)=cos(x/3)')
print('FIXED POINT ITERATION')
print('Initial guess: 0.5')

from math import sin,cos

def f(x): return x*sin(x)-cos(x/3)
def g(x): return cos(x/3)/sin(x)
def dgdx(x): return (sin(x)*-sin(x/3)/3-cos(x/3)*cos(x))/(sin(x))**2

x=0.5
if dgdx(x)<1:
    print('Ok Guess!')
else:
    print('Convergence cannot be achieved')

n=1
while abs(x- g(x))>0.001:
    print('{:3d}'.format(n),': x= {:1.3f}'.format(x),', g(x)= {:1.3f}'.format(g(x)))
    x=g(x)
    n=n+1

s=x    
print('answer= {:1.3f}'.format(s))

input('\nPress return to exit')
    

