print('Newton\'s Method for Systems of Nonlinear Equations')
print('\nSolve for x1, x2, x3 and x4:')
print('8x1 + x2 - 2x3 - 1.5/x4 = 13')
print('2(x1^2)x3 - 5*sqrt(x2) = 0')
print('2.5x2*exp(x1) = x4/x1')
print('20x1/(x2^2) - x3 - 1.8 = 3x4')

from numpy import *
from numpy.linalg import inv

xi=array([[1],[1],[1],[1]])
print('\nInitial guesses= ',xi)

error=zeros((4,1),float)
m=1000
tol=0.001
noit=0

def Fx(x1,x2,x3,x4):
    F=[[8*x1+x2-2*x3-1.5/x4-13],
       [2*(x1**2)*x3-5*sqrt(x2)],
       [2.5*x2*exp(x1)-x4/x1],
       [20*x1/(x2**2)-x3-1.8-3*x4]]
    return F

def Jx(x1,x2,x3,x4):
    J=[[8, 1, -2, 1.5/(x4**2)],
       [4*x3*x1, -5/2/sqrt(x2),2*x1**2, 0],
       [2.5*x2*exp(x1)+x4/(x1**2),2.5*exp(x1),0,-1/x1],
       [20/(x2**2),-40*x1/(x2**3),-1,-3]]
    return J

for n in range(1,m+1):
    x1=xi[0,0]
    x2=xi[1,0]
    x3=xi[2,0]
    x4=xi[3,0]
    
    J=Jx(x1,x2,x3,x4)
    F=Fx(x1,x2,x3,x4)
    xin=xi-dot(inv(J),F)
    error=abs(xin-xi)

    noit=n
    if amax(error)<tol:
        print('\nxin= ',xin)
        print('\nNumber of iterations= ',noit)
        print('\nerror= ',error)
        break
    xi=xin

if noit==m:
    print('Solution does not converge at',noit,'iterations')
    
input('\nPress return to exit')
