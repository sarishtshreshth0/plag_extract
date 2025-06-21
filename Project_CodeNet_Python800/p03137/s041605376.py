N, M = map(int, input().split())
X = sorted([int(i) for i in input().split()])
dx = []
for i in range(1, M):
    dx.append(abs(X[i] - X[i-1]))
dx = sorted(dx)
print(sum(dx[:max(M-N, 0)]))