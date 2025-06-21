from math import *
n,m=map(int,input().split())
if(n==1 or m==1):
    print(1)
else:
    print(ceil((n*m)/2))
