import time
from collections import deque
N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

F = [set() for _ in range(N)]
B = [set() for _ in range(N)]

for i, j in AB:
    F[i - 1].add(j - 1)
    F[j - 1].add(i - 1)
for i, j in CD:
    B[i - 1].add(j - 1)
    B[j - 1].add(i - 1)

Q = deque()
S = [0] * N
d = [0] * N

for i in range(N):
    if d[i] != 0:
        continue
    L = {i}
    d[i] = 1
    Q.append(i)
    while len(Q) > 0:
        q = Q.pop()
        for j in F[q]:
            if d[j] == 0:
                d[j] = 1
                Q.append(j)
                L.add(j)
    for k in L:
        S[k] = len(L) - len(L & F[k]) - len(L & B[k]) - 1

print(*S)
