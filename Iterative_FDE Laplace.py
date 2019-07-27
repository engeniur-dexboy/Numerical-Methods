print('Laplace Equation by Finite Difference Method')

from numpy import *

u2=80
u3=80
u4=80
u8=40
uA=40
u10=150
u11=150
u12=150

u1=0
u9=0

u5=100.0
u6=100.0
u7=100.0

e= 0.001
print('\nn=', 0,': {:5.3f}    {:5.3f}    {:5.3f}'.format(u5,u6,u7))

for i in range (1,101):
    r5=1/4*(u2+u4+u10+u6-4*u5)
    r6=1/4*(u7+u5+u3+u11-4*u6)
    r7=1/6*(u6+u8+8/3*uA+4/3*u12-6*u7)

    u5=u5+r5
    u6=u6+r6
    u7=u7+r7

    print('n=', i,': {:5.3f}    {:5.3f}    {:5.3f}'.format(u5,u6,u7))
    if max(abs(r5),abs(r6),abs(r7))<0.001:
        break

print('\nu5= {:1.3f}'.format(u5))
print('u6= {:1.3f}'.format(u6))
print('u7= {:1.3f}'.format(u7))

input('\nPress return to exit')
