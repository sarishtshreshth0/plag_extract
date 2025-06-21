n, m = map(int, input().split())
X = tuple(map(int, input().split()))
X = sorted(X)
dx = []
for px, bx in zip(X[:m], X[1:]):
    dx.append(bx-px)
if n >= m:
    print(0)
else:
    dx = sorted(dx, reverse=True)
    print(sum(dx[n-1:]))
