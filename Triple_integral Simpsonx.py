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

intsinx=k/3*(sin(e)+sin(f))
intcosx=k/3*(cos(e)+cos(f))
for x in arange(e+2*k,f,2*k):
    intsinx= intsinx+2*k/3*sin(x)
    intcosx= intcosx+2*k/3*cos(x)
for x in arange(e+k,f,2*k):
    intsinx= intsinx+4*k/3*sin(x)
    intcosx= intcosx+4*k/3*cos(x)

int1=j/3*intsinx*(exp(-c)*cos(c)+exp(-d)*cos(d))
int2=j/3*intcosx*(exp(-c)*sin(c)+exp(-d)*sin(d))
for y in arange(c+2*j,d,2*j):
    int1=int1+intsinx*2*j/3*exp(-y)*cos(y)
    int2=int2+intcosx*2*j/3*exp(-y)*sin(y)
for y in arange(c+j,d,2*j):
    int1=int1+intsinx*4*j/3*exp(-y)*cos(y)
    int2=int2+intcosx*4*j/3*exp(-y)*sin(y)

inti=i/3*int1*(a+b)
intii=i/3*int2*(a+b)
for z in arange(a+2*i,b,2*i):
    inti=inti+int1*2*i/3*z
    intii=intii+int2*2*i/3*z
for z in arange(a+i,b,2*i):    
    inti=inti+int1*4*i/3*(z)
    intii=intii+int2*4*i/3*(z)

integral=inti+intii

print('\nvalue of triple integral= ',integral)    

input('\nPress return to exit')
