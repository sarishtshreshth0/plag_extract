n, m = map(int, input().split())
X = sorted(list(map(int, input().split())))
A = []
for a, b in zip(X, X[1:]):
	A.append(b - a)
A.sort()
print(sum(A[:m-n]) if m - n > 0 else 0)