N = int(input())
ad = {}
status = {}
edge=[]

for n in range(N):
    ad[n+1]=set([])
    status[n+1] = -1
    
for n in range(N-1):
    a,b = list(map(int,input().split()))
    edge.append((a,b))
    ad[a].add(b)
    ad[b].add(a)
    
color = set([])
parent = [0] * (N+1) 
ans={}

#BFS
from collections import deque

start = 1
status[start] = 0
que = deque([start])

while len(que) > 0:
    start = que[0]
#     print(start,parent[start])
    c = 1
    for v in ad[start]:
        if status[v] == -1:
            que.append(v)
            status[v]=0
            if parent[start] == c:
                c += 1
            parent[v] = c
            color.add(c)
            
            s = min(start,v)
            e = max(start,v)
            
            ans[s,e]=c
            
            c+=1
            
#     print(parent,que)
    que.popleft()

print(len(color))
for e in edge:
    print(ans[e])