print('RK4 ODE solution')
print('y"','+ (5/6)yy" −(2/3)(y\')^2 +2/3 ; y(0)=y\'(0)=0; y(inf)=1')
import numpy as np
import matplotlib.pyplot as plt


def printSoln(X,Y,freq):
    
    def printHead(n):
        print('\n x ',end=' ')
        for i in range (n):
            print(' y[',i,'] ',end=' ')
    print()

    def printLine(x,y,n):
        print('{:13.4e}'.format(x),end=' ')
        for i in range (n):
            print('{:13.4e}'.format(y[i]),end=' ')
        print()

        
def integrate(F,x,y,xStop,h):

    def run_kut4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)


def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1] - x
    return F

x = 0.0 # Start of integration
xStop = 2.0 # End of integration
y = np.array([0.0, 1.0]) # Initial values of {y}
h = 0.2 # Step size
X,Y = integrate(F,x,y,xStop,h)
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()

input('\nPress return to exit')
