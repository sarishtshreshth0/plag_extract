from collections import deque

N, *ab = map(int, open(0).read().split())
B = ab[1::2]

E = [[] for _ in range(N + 1)]
for a, b in zip(*[iter(ab)] * 2):
    E[a].append(b)

Q = deque([1])
C = [0] * (N + 1)
while Q:
    v = Q.popleft()
    c = 0
    for u in E[v]:
        c += 1 + (c + 1 == C[v])
        C[u] = c
        Q.append(u)

print(max(C))
for b in B:
    print(C[b])
