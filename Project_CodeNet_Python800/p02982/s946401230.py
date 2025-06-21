
import math 

N,D=map(int,input().split())
a=[]
ans=0
for _ in range(N):
    tmp=list(map(int,input().split()))
    a.append(tmp)
for i in range(N-1):
    for k in range(i+1,N):
        dst=0
        for j in range(D):
            dst+=(a[i][j]-a[k][j])**2
        dst=math.sqrt(dst)
        if dst== int(dst):
            ans+=1
print(ans)