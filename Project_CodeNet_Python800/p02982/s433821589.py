from itertools import combinations

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

combi = list(combinations(range(N), 2))

ans = 0
for Y, Z in combi:
    dist = 0
    for i in range(D):
        dist += (X[Y][i] - X[Z][i])**2
    if dist**0.5 <= int(dist**0.5):
        ans += 1

print(ans)
