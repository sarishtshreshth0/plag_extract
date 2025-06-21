import sys
import numpy as np

m = 10**9+7

def syuke(n,r):
    ue=1
    sit=1
    r =min(r,n-r)
    for i in range(r):
        ue = (ue*(n-i))%m
        sit = (sit*(i+1))%m
    return(ue*pow(sit,(m-2),m))

n,a,b = map(int,input().split())

syu = 0
if n<3:
    print(0)
    sys.exit()
syu = pow(2,n,m)-1
syu -= syuke(n,a)%m
syu -= syuke(n,b)%m
print(syu%m)