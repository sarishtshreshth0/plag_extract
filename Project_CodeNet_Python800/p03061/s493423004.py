import random
from operator import itemgetter
import sys
sys.setrecursionlimit(1000000)
ans=0

def gcd(x,y):
    x,y=max(abs(x),abs(y)),min(abs(x),abs(y))
    if x%y==0:
        return y
    while x%y!=0:
        x,y=y,x%y
    return y

def gcd_all(l):
    rt=l.pop()
    for i in l:
        rt=gcd(i,rt)
    return rt
    
n=int(input())

g=[]

a=[int(i) for i in input().split()]

ans=0
d=a[-1]
m=a[-1]
mi=-1
k1=[]
flg=0
for i in range(n):
    gg=gcd(a[i],d)
    if gg<m:
        m=gg
        mi=i
ans=max(ans,gcd_all(a[:mi]+(a[mi+1:] if mi+1<n else [])))

d=a[0]
m=a[0]
mi=0
k1=[]
flg=0
for i in range(n):
    gg=gcd(a[i],d)
    if gg<m:
        m=gg
        mi=i
ans=max(ans,gcd_all(a[:mi]+(a[mi+1:] if mi+1<n else [])))

print(ans)
