print('VAN DER WAAL\'S EQUATION OF STATE')
print('\n1: carbon dioxide\n2: dimethylaniline\n3: helium\n4: nitric oxide')
i = eval(input('Please input number assigned to chosen gas: '))
P = eval(input('Please input pressure in atm: '))
T = eval(input('Please input temperature in K: '))

from numpy import *

R=0.082054
a= array([3.592,37.49,0.03412,1.340])
b= array([0.04267,0.1970,0.0237,0.02789])
ai=a[i-1]
bi=b[i-1]
Tc=8*ai/27/R/bi

def f(v): return (P+ai/v**2)*(v-bi)-R*T
def dfdv(v): return (P+ai/v**2)+(v-bi)*(-2)*v**(-3)

if T>=Tc:
    print('\nSupercritical region')
    v=R*T/P
    for n in range(1,100):
        if dfdv(v)==0:
            print('v not determined')
        else:
            vn=v-f(v)/dfdv(v)
            if abs(vn-v)<=0.001:
                print('molar volume= {:1.3f}'.format(v),' L/mol')
                input('\nPress return to exit')
                break
        v=vn
            
else:
    print('\nSubcritical region')
    
    v1=0.001*R*T/P
    for n in range(1,100):
        if dfdv(v1)==0:
            print('v1 not determined')
        else:
            vn1=v1-f(v1)/dfdv(v1)
            if abs(vn1-v1)<=0.001:
                break
        v1=vn1
             
    v3=R*T/P
    for n in range(1,100):
        if dfdv(v3)==0:
            print('v3 not determined')
        else:
            vn3=v3-f(v3)/dfdv(v3)
            if abs(vn3-v3)<=0.001:
                break
        v3=vn3
        
    x1=1.1*v1
    x3=0.9*v3
    f1=f(x1)
    f3=f(x3)
    while abs(x3-x1)>0.001:
        x2=(x1+x3)/2
        f2=f(x2)
        if f2==0:
            v2=x2
        elif f2*f3<0:
            x1=x2
            f1=f(x2)
            f3=f(x3)
        else:
            x3=x2
            f1=f(x1)
            f3=f(x2)
    v2=x2
    
    if abs(v3-v1)<0.001:
        print('molar volume= {:1.3f}'.format(v1),' L/mol')
    else:
        print('liquid molar volume= {:1.3f}'.format(v1),' L/mol')
        print('non-physical root= {:1.3f}'.format(v2))
        print('vapor molar volume= {:1.3f}'.format(v3),' L/mol')
    
    input('\nPress return to exit')
