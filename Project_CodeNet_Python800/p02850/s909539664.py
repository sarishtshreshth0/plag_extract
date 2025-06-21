from collections import deque

n = int(input())

adj = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    adj[a-1].append([b-1,i])
    adj[b-1].append([a-1,i])

mx_color = 0    
for i in range(n):
    mx_color = max(mx_color,len(adj[i]))

dist = [-1]*n

res = [-1]*(n-1)

q = deque([])
q.append([0,-1])
dist[0] = 0

while len(q) > 0:
    v,c = q.popleft()
    color = 1
    
    if color == c:
        color += 1
        
    for nv,nc in adj[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            q.append([nv,color])
            res[nc] = color
            color += 1
            if color == c:
                color += 1

print(mx_color)

for i in res:
    print(i)
