import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



n,m = map(int, input().split())
from collections import defaultdict
ns = defaultdict(set)
for i in range(m):
    x,y,z = map(int, input().split())
    x -= 1
    y -= 1
    ns[x].add(y)
    ns[y].add(x)
    
seen = [False]*n
ans = 0
for start in range(n):
    if seen[start]:
        continue
    q = [(start, -1)]
    seen[start] = True
    val = None
    while q:
        u, prev = q.pop()
        for v in ns[u]:
            if v==prev:
                continue
            if seen[v]:
                val = 1
            else:
                seen[v] = True
                q.append((v, u))
    if val is None:
        val = 1
    ans += val
print(ans)