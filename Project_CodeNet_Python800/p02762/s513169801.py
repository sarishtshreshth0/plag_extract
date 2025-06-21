from sys import setrecursionlimit
setrecursionlimit(10 ** 5)

def find(parent, i):
    t = parent[i]
    if t < 0:
        return i
    t = find(parent, t)
    parent[i] = t
    return t


def unite(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
        return
    parent[j] += parent[i]
    parent[i] = j

n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(k)]

parent = [-1] * n
friends = [[] for _ in range(n)]

for a, b in ab:
    unite(parent, a-1, b-1)
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)
    
blocks = [[] for _ in range(n)]
for c, d in cd:
    blocks[c-1].append(d-1)
    blocks[d-1].append(c-1)

result = []

for i in range(n):
    p = find(parent, i)
    t = -parent[p] - 1
    t -= len(friends[i])
    for b in blocks[i]:
        if p == find(parent, b):
            t -= 1
    result.append(t)
    
print(*result)