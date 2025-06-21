N, M = map(int, input().split())
X = list(map(int, input().split()))
if N >= M:
    print(0)
    exit()
X.sort()
Y = []
for i in range(1, M):
    Y.append(X[i] - X[i - 1])
Y.sort()
ans = sum(Y[:M-N])
print(ans)
