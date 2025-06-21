N,D=map(int,input().split())
X=[list(map(int,input().split())) for _ in range(N)]
ans = 0
from itertools import combinations
from os import kill
for i, j in combinations(range(N), 2):
    d = sum([(X[i][k]-X[j][k])**2 for k in range(D)])
    if int(d**0.5) == d**0.5:
        ans += 1
print(ans)