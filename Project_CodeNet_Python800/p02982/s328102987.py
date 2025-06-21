from math import sqrt as r
from itertools import combinations as C

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

L = list(C(list(range(N)), 2))


def dis(a, b):
    ans = 0
    for i in range(D):
        ans += (X[a][i] - X[b][i])**2
    return r(ans)


ans = 0

for l in L:
    ans_ = dis(l[0], l[1])
    if str(ans_)[-1] == "0":
        ans += 1

print(ans)
