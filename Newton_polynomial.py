print('Newton\'s Polynomial Extrapolation')
print('Find y-value at x=6.5')

from numpy import *

def coeffts(xData,yData):
    m = len(xData)
    a = yData.copy()
    for k in range(1,m):
        for i in range(k,m):
            a[i] = (a[i] - a[k-1])/(xData[i] - xData[k-1])
    return a

def evalPoly(a,xData,x):
    n = len(xData) - 1
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xData[n-k])*p
    return p

x=array([1,2,3,4,5,6])
y=array([0.9,2,2.5,3.5,3.6,4])
print('\nxData= ',x)
print('yData= ',y)

an=coeffts(x,y)
F= zeros((6,7),float)
for i in range(0,6):
    F[i,0]=x[i]
    F[i,1]=y[i]

for j in range(2,7):
    for k in range(j-1,6):
        F[k,j]=(F[k,j-1]-F[k-1,j-1])/(F[k,0]-F[k-j+1,0])
print('\n      x       f(x)       f\'         f"         f"\'      f""      f""\'')
print('------------------------------------------------------------------------')
set_printoptions(formatter={'float': '{: 0.6f}'.format})
print(F)
    
pn=evalPoly(an,x,6.5)
print('\nanswer= {:1.9f}'.format(pn))

import matplotlib.pyplot as plt
t=arange(0.0,7,0.1)
plt.plot(t,evalPoly(an,x,t))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
data = [[1,0.9],[2,2],[3,2.5],[4,3.5],[5,3.6],[6,4]]
plt.plot(*zip(*data), marker='o', color='r', ls='')
xp = [[6.5,pn]]
plt.plot(*zip(*xp), marker='o', color='g', ls='')
plt.title('NEWTON POLYNOMIAL')
plt.show()

input('\nPress return to exit')
