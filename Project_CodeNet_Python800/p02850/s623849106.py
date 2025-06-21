n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append([b-1,i])
    g[b-1].append([a-1,i])
from collections import deque
d = deque([(0,-1)])
ans = [0 for i in range(n-1)]
while d:
    a,noc = d.popleft()
    c = 1 if noc != 1 else 2
    for b,i in g[a]:
        if ans[i] == 0:
            ans[i] = c
            d.append((b,c))
        else:
            continue
        c += 1 if c+1 != noc else 2
print(max(ans))
for i in range(n-1):
    print(ans[i])