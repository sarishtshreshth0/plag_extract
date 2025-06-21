N, D = list(map(int, input().split()))
XS = [[0] * D for _ in range(N)]
for i in range(N):
	XS[i] = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
	for j in range(i + 1, N):
		c1 = 0
		for k in range(D):
			c1 += (XS[i][k] - XS[j][k]) ** 2
		c2 = c1 ** 0.5
		if c2 == int(c2):
			ans += 1
print(ans)
