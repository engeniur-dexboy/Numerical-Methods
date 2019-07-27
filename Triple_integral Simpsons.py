print('TRIPLE INTEGRAL BY COMPOSITE SIMPSON\'s RULE, n=10')
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

N=10
i=(b-a)/(2*N)
j=(d-c)/(2*N)
k=(f-e)/(2*N)

int1x=k/3*(sin(e)+sin(f))
int2x=k/3*(cos(e)+cos(f))
for x in range(1,N):
    int1x= int1x+2*k/3*sin(e+2*x*k)
    int2x= int2x+2*k/3*cos(e+2*x*k)
for x in range(1,N+1):
    int1x= int1x+4*k/3*sin(e+(2*x-1)*k)
    int2x= int2x+4*k/3*cos(e+(2*x-1)*k)
print('\nI1x= {:3.6f}'.format(int1x))
print('I2x= {:3.6f}'.format(int2x))

int1y=j/3*(exp(-c)*cos(c)+exp(-d)*cos(d))
int2y=j/3*(exp(-c)*sin(c)+exp(-d)*sin(d))
for y in range(1,N):
    int1y=int1y+2*j/3*exp(-c-2*y*j)*cos(c+2*y*j)
    int2y=int2y+2*j/3*exp(-c-2*y*j)*sin(c+2*y*j)
for y in range(1,N+1):
    int1y=int1y+4*j/3*exp(-c-(2*y-1)*j)*cos(c+(2*y-1)*j)
    int2y=int2y+4*j/3*exp(-c-(2*y-1)*j)*sin(c+(2*y-1)*j)
int1xy=int1y*int1x
int2xy=int2y*int2x
print('\nI1xy= {:3.6f}'.format(int1xy))
print('I2xy= {:3.6f}'.format(int2xy))

int1z=i/3*(a+b)
int2z=i/3*(a+b)
for z in range(1,N):
    int1z=int1z+2*i/3*(a+2*z*i)
    int2z=int2z+2*i/3*(a+2*z*i)
for z in range(1,N+1):
    int1z=int1z+4*i/3*(a+(2*z-1)*i)
    int2z=int2z+4*i/3*(a+(2*z-1)*i)
int1xyz=int1xy*int1z
int2xyz=int2xy*int2z    
print('\nI1xyz= {:3.6f}'.format(int1xyz))
print('I2xyz= {:3.6f}'.format(int2xyz))

integral=int1xyz+int2xyz
print('\nvalue of triple integral= {:3.6f}'.format(integral))  

input('\nPress return to exit')
