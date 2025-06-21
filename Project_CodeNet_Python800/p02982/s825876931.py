# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
import math
import itertools
input = sys.stdin.readline

N, D = map(int, input().split())
P = []
for i in range(N):
    P.append(list(map(int, input().split())))
ans = 0
for c in itertools.combinations(range(N), 2):
    i = c[0]
    j = c[1]
    dis = 0
    for k in range(D):
        dis += (P[j][k] - P[i][k])**2
    if math.sqrt(dis) == int(math.sqrt(dis)):
        ans += 1
print(ans)
