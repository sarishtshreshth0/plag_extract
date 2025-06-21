
N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
diff = sorted(X[i + 1] - X[i] for i in range(M - 1))
print(sum(diff[:max(0, M - N)]))
