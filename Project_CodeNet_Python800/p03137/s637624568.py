n, m = map(int, input().split())
X = sorted(list(map(int, input().split())))
if n >= m : print(0)
else:
    d = sorted([i-j for i, j in zip(X[1:], X)])
    print(sum(d[:m-n]))
