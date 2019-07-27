print('Derivative of Newton\'s Polynomial')
print('Find derivative at x=3')

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

def NPdfdx(a, xData,x):
    n = len(xData) - 1
    p = a[n]
    dpdx=0
    for k in range(1,n+1):
        dpdx=p+(x -xData[n-k])*dpdx
        p = a[n-k] + (x -xData[n-k])*p
    return dpdx

xArray=array([1,2,3,4,5,6])
yArray=array([0.9,2,2.5,3.5,3.6,4])
print('\nxData= ',xArray)
print('yData= ',yArray)

an=coeffts(xArray,yArray)
dfdx=NPdfdx(an,xArray, 3)
print('\nh-value        derivative[CD O(h^4)]  derivative(NP)   error')
print('--------------------------------------------------------------------')

for j in range (1,10):
    h=10**(-j)   
    dprime=(-evalPoly(an, xArray, 3+2*h)+8*evalPoly(an, xArray, 3+h)-8*evalPoly(an, xArray, 3-h)+evalPoly(an, xArray, 3-2*h))/(12*h)
    error= dprime-dfdx
    print('{:3.9f}    {:3.9f}            {:3.9f}      {:3.9f}'.format(h,dprime,dfdx,error))

input('\nPress return to exit')
