n,d = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(n)]

def dist_squere(x, y):
    d = 0
    for i,j in zip(x,y):
        d += (i-j)**2
    return d**.5

from itertools import combinations

ans = 0
for x,y in combinations(X, 2):
    if dist_squere(x, y).is_integer():
        ans += 1

print(ans)