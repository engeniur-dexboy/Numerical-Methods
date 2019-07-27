print('Gauss-Seidel Iteration for Systems of Linear Equations')

from numpy import *
print('Data:')

data = open('datafile.txt','r')
n=int(eval(data.readline()))
print('matsize= {:00}'.format(n))

Mo=loadtxt(data.readlines()[0:4])
M=array(Mo)

A= zeros((n,n),float)
for j in range(0,n):
    for i in range(0,n):
        A[i,j]=M[i,j]
print('\nA= ',A)

bT= zeros((1,n),float)
for i in range(0,n):
    bT[0,i]=M[n,i]
b=transpose(bT)
print('\nb= ',b,'\n')

xT = [eval(input('Please input guesses for solution: ')) for l in range(n)]
xT=array([xT])
xo=transpose(xT)
print('xo= ',xo)

m= eval(input('Please input maximum number of iterations(~1000): '))
tol = eval(input('Please input tolerance(~0.001): '))

xi= zeros((m+1,n),float)
ci= zeros((n,1),float)
bik= zeros((n,n),float)
error= zeros((1,n),float)
noit=0

for i in range(0,n):
    ci[i,0]=(b[i,0])/(A[i,i])
    for j in range(0,n):
        if i==j:
            bik[i,j]=0
        else:
            bik[i,j]=-A[i,j]/A[i,i]
print('\nci= ',ci)
print('\nbik= ',bik)
    
for i in range(0,n):
    xi[0,i]=xT[0,i]

for v in range(0,m):
    for i in range(0,n):
        Brxi=0
        for r in range(i,n):
            Brxi=Brxi+bik[i,r]*xi[v,r]
        Blxi=0
        for l in range(0,i):
            Blxi=Blxi+bik[i,l]*xi[v+1,l]
        xi[v+1,i]=ci[i,0]+Brxi+Blxi
        error[0,i]=abs(xi[v+1,i]-xi[v,i])
    noit=v
    if amax(error)<tol:
        print('\nNumber of iterations =',noit)
        print('error= ',error)
        break

xi.resize((noit+1,n))
print('\nxi= ',xi)

if amax(error)>=tol:
    print('\nConvergence not achieved')
    print('error= ',error)

input('\nPress return to exit')
