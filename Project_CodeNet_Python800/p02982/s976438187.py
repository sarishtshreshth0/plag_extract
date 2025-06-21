import math
a,b=map(int,input().split())
c=[]
for _ in range(a):
    c.append(list(map(int,input().split())))
ans=0
for i in range(a):
    for j in range(i):
        n=c[i]
        m=c[j]
        result=[(x-y)**2 for (x,y) in zip(n,m)]
        if math.sqrt(sum(result))%1==0:
            ans+=1
print(ans)
