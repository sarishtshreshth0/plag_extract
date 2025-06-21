from decimal import Decimal
import math
n,d=map(int,input().split())
x=[]
ans=0
for i in range(n):
    x.append(list(map(int,input().split())))
for i in range(n-1):
    for j in range(i+1,n):
        tmp=0
        for k in range(d):
            tmp+=(x[i][k]-x[j][k])**2
        tt=math.sqrt(tmp)
        if tt==int(tt):
            ans+=1
print(ans)