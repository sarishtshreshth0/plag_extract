import numpy as np
import itertools

n, d = map(int,input().split())
x = np.array([list(map(int,input().split())) for i in range(n)])

i = 1
sq = []
while i**2 <= 40**2*10:
    sq.append(i**2)
    i += 1

cnt = 0
l = [int(i) for i in range(n)]
for v in itertools.combinations(l, 2):
    i, j = v[0], v[1]
    sub = x[i] - x[j]
    dist = sum(sub**2)
    if dist in sq:
        cnt += 1
print(cnt)