from itertools import combinations
N, D = map(int, input().split())
X = [tuple(map(int, input().split())) for _ in range(N)]
res = 0
for i, j in combinations(list(range(N)), 2):
    tmp = sum((y - z) ** 2 for y, z in zip(X[i], X[j]))
    tmp **= 0.5
    if tmp == int(tmp):
        res += 1
print(res)