print('Find the smallest positive value of x in xsin(x)=cos(x/3)')
print('NEWTON\'S METHOD')
print('Initial guess: 0.5')

from math import sin,cos

def f(x): return x*sin(x)-cos(x/3)
def dfdx(x): return x*cos(x)+sin(x)+(sin(x/3))/3

x=0.5
print('  0 : x={:1.3f}'.format(x))

for n in range(1,100):
    if dfdx(x)==0:
        print('Procedure completed unsuccesfully')
    else:
        xn=x-f(x)/dfdx(x)
        print('{:3d}'.format(n),': x={:1.3f}'.format(xn))
        if abs(xn-x)<=0.001:
            print('answer= {:1.3f}'.format(x))
            input('\nPress return to exit')
            break
        x=xn

    
    

