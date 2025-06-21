N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
dif = []

for i in range(1, M):
	dif.append(abs(X[i] - X[i-1]))

dif.sort()
difLen = len(dif)
# M - N = (M-1) - (N-1)
e = M - N
if e < 0:
	print(0)
	exit()
ans = sum(dif[0:e])

print(ans)