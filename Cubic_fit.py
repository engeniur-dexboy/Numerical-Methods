print('FIT CUBIC POLYNOMIAL TO DATA')

from numpy import *
from numpy.linalg import inv

x=array([1,2,3,4,5,6])
y=array([0.9,2,2.5,3.5,3.6,4])
print('xData= ',x)
print('yData= ',y)

sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
sumyx3=0
sumyx2=0
sumyx=0
sumy=0
for i in range(0,6):
    sum1=sum1+x[i]
    sum2=sum2+(x[i])**2
    sum3=sum3+(x[i])**3
    sum4=sum4+(x[i])**4
    sum5=sum5+(x[i])**5
    sum6=sum6+(x[i])**6
    sumyx3=sumyx3+(y[i])*(x[i])**3
    sumyx2=sumyx2+(y[i])*(x[i])**2
    sumyx=sumyx+(y[i])*(x[i])
    sumy=sumy+y[i]
    
A=array([[sum6, sum5, sum4, sum3],[sum5, sum4, sum3, sum2],[sum4, sum3, sum2, sum1],[sum3, sum2, sum1,6]])
print('\nA= ',A)

b=array([[sumyx3],[sumyx2],[sumyx],[sumy]])
print('\nB= ',b)

c=dot(inv(A),b)
print('\ny = ({:1.6f}'.format(c[0,0]),')x^3 + ({:1.6f}'.format(c[1,0]),')x^2 + ({:1.6f}'.format(c[2,0]), ')x + ({:1.6f}'.format(c[3,0]),')')

E=0
Em=0
for j in range(0,6):
    ycalc=c[0,0]*x[j]**3+c[1,0]*x[j]**2+(c[2,0])*x[j]+c[3,0]
    E=(y[j]-ycalc)**2+E
    Em=(y[j]-sumy/6)**2+Em
rsquared= 1-E/Em
print('r^2 = {:1.6f}'.format(rsquared))

import matplotlib.pyplot as plt
x=arange(0.0,6.5,0.2)
plt.plot(x,c[0,0]*x**3+c[1,0]*x**2+(c[2,0])*x+c[3,0])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
data = [[1,0.9],[2,2],[3,2.5],[4,3.5],[5,3.6],[6,4]]
plt.plot(*zip(*data), marker='o', color='r', ls='')
plt.title('FIT CUBIC POLYNOMIAL TO DATA')
plt.show()

input('\nPress return to exit')
