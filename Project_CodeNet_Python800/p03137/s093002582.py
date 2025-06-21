N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))
Y = sorted([X[i+1]-X[i] for i in range(M-1)])[::-1]
print(max(X)-min(X)-sum(Y[:N-1]))