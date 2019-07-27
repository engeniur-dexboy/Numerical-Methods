print('Spline Approximation')

from numpy import *
from numpy.linalg import inv

inputfile=input('\nInput data points: ')

data = open(inputfile,'r')
N=int(eval(data.readline()))
M=array(loadtxt(data.readlines()))

A=zeros((N,N),float)
b=zeros((N,1),float)

A[0,0]=1
A[1,N-1]=1
for j in range(2,N):
    A[j,j-2]=(M[j-1,0]-M[j-2,0])/6
    A[j,j-1]=(M[j,0]-M[j-2,0])/3
    A[j,j]=(M[j,0]-M[j-1,0])/6
    b[j,0]=(M[j,1]-M[j-1,1])/(M[j,0]-M[j-1,0])-(M[j-1,1]-M[j-2,1])/(M[j-1,0]-M[j-2,0])
c=dot(inv(A),b)

print('\nThe natural cubic spline through the given data points')
print('consists of cubic functions: ')
for i in range(1,N):
    an=(c[i,0]-c[i-1,0])/(6*(M[i,0]-M[i-1,0]))
    bn=(3*M[i,0]*c[i-1,0]-3*M[i-1,0]*c[i,0])/(6*(M[i,0]-M[i-1,0]))
    cn=((-M[i,0]**2)*c[i-1,0]+(M[i-1,0]**2)*c[i,0])/(2*(M[i,0]-M[i-1,0]))+(-M[i-1,1]+M[i,1])/(M[i,0]-M[i-1,0])-1/6*((-M[i,0]+M[i-1,0])*c[i-1,0]+(M[i,0]-M[i-1,0])*c[i,0])
    dn=((M[i,0]**3)*c[i-1,0]-(M[i-1,0]**3)*c[i,0])/(6*(M[i,0]-M[i-1,0]))+(M[i,0]*M[i-1,1]-M[i-1,0]*M[i,1])/(M[i,0]-M[i-1,0])-1/6*((M[i,0]**2-M[i-1,0]*M[i,0])*c[i-1,0]+(-M[i-1,0]*M[i,0]+M[i-1,0]**2)*c[i,0])
    print('({:2.3f}'.format(M[i-1,0]),', {:2.3f}'.format(M[i,0]),'): y= ({:2.6f}'.format(an),')x^3 + ({:2.6f}'.format(bn),')x^2 + ({:2.6f}'.format(cn),')x +({:2.6f}'.format(dn),')')

x=eval(input('\nInput value of x where to approximate the function: '))

print('\nUsing the spline, the value of y at x =',x,'is')
for k in range (1,N):
    if x<=M[k,0] and x>=M[k-1,0]:
        ax=(c[k,0]-c[k-1,0])/(6*(M[k,0]-M[k-1,0]))
        bx=(3*M[k,0]*c[k-1,0]-3*M[k-1,0]*c[k,0])/(6*(M[k,0]-M[k-1,0]))
        cx=((-M[k,0]**2)*c[k-1,0]+(M[k-1,0]**2)*c[k,0])/(2*(M[k,0]-M[k-1,0]))+(-M[k-1,1]+M[k,1])/(M[k,0]-M[k-1,0])-1/6*((-M[k,0]+M[k-1,0])*c[k-1,0]+(M[k,0]-M[k-1,0])*c[k,0])
        dx=((M[k,0]**3)*c[k-1,0]-(M[k-1,0]**3)*c[k,0])/(6*(M[k,0]-M[k-1,0]))+(M[k,0]*M[k-1,1]-M[k-1,0]*M[k,1])/(M[k,0]-M[k-1,0])-1/6*((M[k,0]**2-M[k-1,0]*M[k,0])*c[k-1,0]+(-M[k-1,0]*M[k,0]+M[k-1,0]**2)*c[k,0])
        y=ax*x**3+bx*x**2+cx*x+dx
        print('{:2.3f}'.format(y))
        break

input('\nPress return to exit')
  
