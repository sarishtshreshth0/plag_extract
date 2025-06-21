import numpy as np
N,D=map(int,input().split())
X=[np.array(input().split(),dtype=np.int64) for _ in range(N)]
ans=0
for i in range(N):
    for j in range(i+1,N):
        d=((X[i]-X[j])*(X[i]-X[j])).sum()
        dd=int(round(d**.5))
        if d==dd*dd:
            ans +=1
print(ans)