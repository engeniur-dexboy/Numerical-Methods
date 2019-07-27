print('Response of a two-storey building model with negligible damping to')
print('an earthquake-induced ground acceleration (ODE solution by RK4)')

from numpy import *
from numpy.linalg import inv
import matplotlib.pyplot as plt

print('\nObtaining data from Kobe1995.txt from 0 to 20s')

data = open('Kobe1995.txt','r')
Ag=array(loadtxt(data.readlines()[1:1003]))
F=zeros((2002,6),float)

for i in range (0,2002):
    F[i,0]=0+0.01*i

for i in range (0,1001):
    F[2*i,1]=Ag[i,1]
    F[2*i+1,1]=(Ag[i,1]+Ag[i+1,1])/2

h=0.01

for i in range (1,2001):
    k1=F[i-1,3]
    g1=(-50*F[i-1,1]-30*F[i-1,2]+10*F[i-1,4])/50
    m1=F[i-1,5]
    n1=(-50*F[i-1,1]+10*F[i-1,2]-10*F[i-1,4])/50
    
    k2=F[i-1,3]+h/2*g1
    g2=(-50*(F[i-1,1]+F[i,1])/2-30*(F[i-1,2]+h/2*k1)+10*(F[i-1,4]+h/2*m1))/50
    m2=F[i-1,5]+h/2*n1
    n2=(-50*(F[i-1,1]+F[i,1])/2+10*(F[i-1,2]+h/2*k1)-10*(F[i-1,4]+h/2*m1))/50

    k3=F[i-1,3]+h/2*g2
    g3=(-50*(F[i-1,1]+F[i,1])/2-30*(F[i-1,2]+h/2*k2)+10*(F[i-1,4]+h/2*m2))/50
    m3=F[i-1,5]+h/2*n2
    n3=(-50*(F[i-1,1]+F[i,1])/2+10*(F[i-1,2]+h/2*k2)-10*(F[i-1,4]+h/2*m2))/50

    k4=F[i-1,3]+h*g3
    g4=(-50*F[i,1]-30*(F[i-1,2]+h*k3)+10*(F[i-1,4]+h*m3))/50
    m4=F[i-1,5]+h*n3
    n4=(-50*F[i,1]+10*(F[i-1,2]+h*k3)-10*(F[i-1,4]+h*m3))/50

    F[i,2]=F[i-1,2]+h/6*(k1+2*k2+2*k3+k4)
    F[i,3]=F[i-1,3]+h/6*(g1+2*g2+2*g3+g4)
    F[i,4]=F[i-1,4]+h/6*(m1+2*m2+2*m3+m4)
    F[i,5]=F[i-1,5]+h/6*(n1+2*n2+2*n3+n4)

print('\ntime(s)        ag(m/s2)            u1(m)            u1\'(m/s)          u2(m)           u2\'(m/s)')

for i in range (0,21):
    time=F[100*i,0]
    agrav=F[100*i,1]
    uone=F[100*i,2]
    uonedot=F[100*i,3]
    utwo=F[100*i,4]
    utwodot=F[100*i,5]
    print('{:3.2f}        {:3.9f}         {:3.9f}       {:3.9f}      {:3.9f}      {:3.9f}'.format(time,agrav,uone,uonedot,utwo,utwodot))

print('\nFor sample calculations:')
for i in range (0,3):
    time=F[1000+i,0]
    agrav=F[1000+i,1]
    uone=F[1000+i,2]
    uonedot=F[1000+i,3]
    utwo=F[1000+i,4]
    utwodot=F[1000+i,5]
    print('{:3.2f}        {:3.9f}         {:3.9f}       {:3.9f}      {:3.9f}      {:3.9f}'.format(time,agrav,uone,uonedot,utwo,utwodot))

t=transpose(F[0:2001,0])
u1=transpose(F[0:2001,2])
u2=transpose(F[0:2001,4])
plt.plot(t,u1, t, u2)
plt.xlabel('time (in seconds)')
plt.ylabel('floor displacement (in meters)')
plt.legend(('first level','second level'),loc = 0)
plt.grid(True)
plt.show()
    
input('\nPress return to exit')
