from math import *
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
c=0
for i in range(n-1):
    for j in range(i+1,n):
        d=0
        for k in range(m):
            d+=(l[i][k]-l[j][k])**2
        dd=sqrt(d)
        if(int(dd)==dd):
            c+=1
print(c)
