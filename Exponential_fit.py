print('FIT EXPONENTIAL FUNCTION (y=axe^bx) TO DATA')

from numpy import *
from numpy.linalg import inv

x=array([1,2,3,4,5,6])
y=array([0.9,2,2.5,3.5,3.6,4])
print('xData= ',x)
print('yData= ',y)

Y=array([log(0.9/1),log(2/2),log(2.5/3),log(3.5/4),log(3.6/5),log(4/6)])

sum1=0
sum2=0
sumxY=0
sumY=0
sumy=0
for i in range(0,6):
    sum1=sum1+x[i]
    sum2=sum2+(x[i])**2
    sumxY=sumxY+(x[i])*(Y[i])
    sumY=sumY+Y[i]
    
A=array([[sum2, sum1],[sum1, 6]])
print('\nA= ',A)

B=array([[sumxY],[sumY]])
print('\nB= ',B)

c=dot(inv(A),B)
b=c[0,0]
a=exp(c[1,0])
print('\ny = {:1.6f}'.format(a),'(x)exp({:1.6f}'.format(b),'x)')

E=0
Em=0
for j in range(0,6):
    Ycalc=b*x[j]+log(a)
    E=(Y[j]-Ycalc)**2+E
    Em=(Y[j]-sumY/6)**2+Em
rsquared= 1-E/Em
print('r^2 = {:1.6f}'.format(rsquared))

import matplotlib.pyplot as plt
x=arange(0.0,6.5,0.2)
plt.plot(x,a*x*exp(b*x))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
data = [[1,0.9],[2,2],[3,2.5],[4,3.5],[5,3.6],[6,4]]
plt.plot(*zip(*data), marker='o', color='r', ls='')
plt.title('FIT EXPONENTIAL FUNCTION TO DATA')
plt.show()

input('\nPress return to exit')
