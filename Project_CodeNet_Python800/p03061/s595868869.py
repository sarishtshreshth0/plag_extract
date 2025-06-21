n=int(input())
*a,=map(int,input().split())
a=sorted(a)
from math import gcd

for i in range(n):
    if i==0:
        tmp=a[i]
    else:
        tmp=gcd(tmp, a[i])

b=[x//tmp for x in a]

for i in range(n):
    if i==0:
        tmp=b[i]
    else:
        tmp=gcd(tmp, b[i])
        if tmp==1:
            l=i-1
            r=i
            break
if l>0:
    c=a[:l]+a[l+1:]
else:
    c=a[1:]
if r+1<n:
    d=a[:r]+a[r+1:]
else:
    d=a[:r]

for i in range(len(c)):
    if i==0:
        ctmp=c[i]
        dtmp=d[i]
    else:
        ctmp=gcd(ctmp, c[i])
        dtmp=gcd(dtmp, d[i])

ans=max(ctmp,dtmp)

for i in range(n-1,-1,-1):
    if i==n-1:
        tmp=b[i]
    else:
        tmp=gcd(tmp, b[i])
        if tmp==1:
            l=i
            r=i+1
            break
if l>0:
    c=a[:l]+a[l+1:]
else:
    c=a[1:]
if r+1<n:
    d=a[:r]+a[r+1:]
else:
    d=a[:r]

for i in range(len(c)):
    if i==0:
        ctmp=c[i]
        dtmp=d[i]
    else:
        ctmp=gcd(ctmp, c[i])
        dtmp=gcd(dtmp, d[i])

print(max(ans,ctmp,dtmp))