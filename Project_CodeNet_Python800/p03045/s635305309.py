from collections import *
n,m=map(int,input().split())
v=[False for i in range(n)]
t=[[]for i in range(n)]
for i in range(m):
    x,y,z=map(int,input().split())
    x,y=x-1,y-1
    t[x].append(y)
    t[y].append(x)
ans=0
for i in range(n):
    if v[i]:
        continue
    else:
        ans+=1
        for j in t[i]:
            q=deque()
            if v[j]==False:
                q.append(j)
                while q:
                    k=q.popleft()
                    v[k]=True
                    for l in t[k]:
                        if v[l]==False:
                            q.append(l)
print(ans)
