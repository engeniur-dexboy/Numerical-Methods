print('Eigenvalues and Eigenvectors of Matrix A')
print('Shifted-Inverse Power Method')

from numpy import *
from numpy.linalg import inv

C1=array([[50,0],
          [0,50]])
print('\nC1= ')
print(C1)

C2=array([[30,-10],
          [-10,10]])
print('\nC2= ')
print(C2)

A=dot(inv(C1),C2)
print('\nA= inv(C1)x C2= ')
print(A)

s= 2
I= identity(2)
alpha=0

x0=[1,1]
N= 100
e = 0.000001

print('\nalpha= ',alpha)
print('x0=',x0)
set_printoptions(formatter={'float': '{: 1.6f}'.format})

for i in range (1,N+1):
    y=dot(inv(A-alpha*I),transpose(x0))
    cmax=amax(y)
    cmin=amin(y)
    if cmax>=abs(cmin):
        c=cmax
    else:
        c=cmin
    x1=transpose(dot(1/c,y))
    print(i,': x = ',x1)
    if amax(abs(x1-x0))<e:
       print('\nc = {: 1.6f}'.format(c))
       break
    x0=x1


print('Dominant eigenvalue : {: 1.6f}'.format(1/c+alpha))
print('Dominant eigenvector: ',x1)

input('\nPress return to exit')
