N, M = map(int, input().split())
X = list(sorted(map(int, input().split())))

L = [0] * (M - 1)
for i in range(1, M):
    L[i - 1] = X[i] - X[i - 1]

L = sorted(L, reverse=True)

print(sum(L[N - 1:]))
