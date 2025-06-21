import math
n,d=map(int,input().split())
x=[]
for _ in range(n):
    x.append(list(map(int,input().split())))
ans=0
i=0
for i in range(n-1):
    for j in range(i+1,n):
        l2=0
        for k in range(d):
            l2+=(x[i][k]-x[j][k])**2
        if math.ceil(math.sqrt(l2))==math.floor(math.sqrt(l2)):
            ans+=1
print(ans)
