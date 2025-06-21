from collections import deque
N,M = map(int,input().split())
E = [[] for _ in range(N+1)]
for i in range(M):
    x,y,z = map(int,input().split())
    E[x].append(y)
    E[y].append(x)

d = [-1]*(N+1)

def dfs(start,num):
    q = deque([start])
    d[start] = num
    while(q):
        v = q.pop()
        for s in E[v]:
            if(d[s] == -1):
                d[s] = num
                q.append(s)

group_num = 0
for i in range(1,N+1):
    if(d[i] == -1):
        group_num += 1
        dfs(i,group_num)

print(group_num)        