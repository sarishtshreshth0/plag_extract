import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


from collections import defaultdict
n = int(input())
ns = defaultdict(set)
uvs = [None]*(n-1)
for i in range(n-1):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add(v)
    ns[v].add(u)
    uvs[i] = (u,v)

s = [(0, -1)]
cs = {(0,-1): -1}
seen = [False]*n
seen[0] = True
while s:
    u,prev = s.pop()
    val = 0
    cc = cs[u,prev]
    for v in ns[u]:
        if seen[v]:
            continue
        if val==cc:
            val += 1
        cs[v,u] = val
        val += 1
        seen[v] = True
        s.append((v,u))
ans = []
for u,v in uvs:
    if (u,v) in cs:
        ans.append(cs[u,v]+1)
    else:
        ans.append(cs[v,u]+1)
print(max(ans))
write("\n".join(map(str, ans)))