from collections import deque
n,m,k=map(int,input().split())
fl=[set() for _ in range(n+1)]
bl=[set() for _ in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  fl[a].add(b)
  fl[b].add(a)
for i in range(k):
  c,d=map(int,input().split())
  bl[c].add(d)
  bl[d].add(c)
stack = deque()
ans = [0]*(n+1)
visited = [0]*(n+1)
for i in range(1, n+1):
    if visited[i]:
        continue
    link = {i}
    visited[i] = 1
    stack.append(i)
    while stack:
        n = stack.pop()
        for j in fl[n]:
            if visited[j] == 0:
                stack.append(j)
                visited[j] = 1
                link.add(j)
    for i in link:
        ans[i] = len(link) - len(link & fl[i]) - len(link & bl[i]) -1
print(*ans[1:])