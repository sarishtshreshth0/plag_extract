from collections import deque

LI = lambda: list(map(int, input().split()))

n, m, k = LI()
adj = [[] for i in range(n)]
for i in range(m):
    a, b = LI()
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
c = []
d = []
for i in range(k):
    tmp = LI()
    c.append(tmp[0]-1)
    d.append(tmp[1]-1)

cc = [i for i in range(n)]
num = [0 for i in range(n)]
for i in range(n):
    if cc[i] == i:
        dq = deque([i])
        while dq:
            j = dq.popleft()
            for l in adj[j]:
                if cc[l] != i:
                    cc[l] = i
                    num[i] += 1
                    dq.append(l)

sf = []
for i in range(n):
    sf.append(num[cc[i]])

for i in range(n):
    sf[i] -= len(adj[i])

for i in range(k):
    if cc[c[i]] == cc[d[i]]:
        sf[c[i]] -= 1
        sf[d[i]] -= 1

print(' '.join(map(str, sf)))