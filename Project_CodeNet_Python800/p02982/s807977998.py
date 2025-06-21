import itertools
n, d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for a, b in itertools.combinations(X, r=2):
    s = (sum(map(lambda x, y: (x - y)**2, a, b)))**0.5
    if s.is_integer():
        ans += 1
print(ans)