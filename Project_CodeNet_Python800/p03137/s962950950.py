n, m = map(int, input().split())
X = sorted(list(map(int, input().split())))
A = []
for a, b in zip(X, X[1:]):
	A.append(b - a - 1)
A.sort(reverse = True)
print(X[-1] - X[0] + 1 - sum(A[:n-1]) - n if n < m else 0)