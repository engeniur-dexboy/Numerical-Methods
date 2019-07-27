print('TRIPLE INTEGRAL BY COMPOSITE TRAPEZOIDAL RULE, n=20')
print('triple integral of z(e^-y)sin(x+y) with respect to dx dy dz')
print('x=0 to 1, y=-1 to 1, and z= pi/5 to pi/4')

from numpy import *
from math import sin,cos

a=0
b=1
c=-1
d=1
e=pi/5
f=pi/4

N=20
i=(b-a)/N
j=(d-c)/N
k=(f-e)/N

int1x=k/2*(sin(e)+sin(f))
int2x=k/2*(cos(e)+cos(f))
for x in range(1,N):
    int1x= int1x+k*sin(e+k*x)
    int2x= int2x+k*cos(e+k*x)
print('\nI1x= {:3.6f}'.format(int1x))
print('I2x= {:3.6f}'.format(int2x))

int1y=j/2*(exp(-c)*cos(c)+exp(-d)*cos(d))
int2y=j/2*(exp(-c)*sin(c)+exp(-d)*sin(d))
for y in range(1,N):
    int1y=int1y+j*exp(-c-j*y)*cos(c+j*y)
    int2y=int2y+j*exp(-c-j*y)*sin(c+j*y)
int1xy=int1y*int1x
int2xy=int2y*int2x
print('\nI1xy= {:3.6f}'.format(int1xy))
print('I2xy= {:3.6f}'.format(int2xy))

int1z=i/2*(a+b)
int2z=i/2*(a+b)
for z in range(1,N):
    int1z=int1z+i*(a+i*z)
    int2z=int2z+i*(a+i*z)
int1xyz=int1xy*int1z
int2xyz=int2xy*int2z    
print('\nI1xyz= {:3.6f}'.format(int1xyz))
print('I2xyz= {:3.6f}'.format(int2xyz))

integral=int1xyz+int2xyz
print('\nvalue of triple integral= {:3.6f}'.format(integral))  

input('\nPress return to exit')
