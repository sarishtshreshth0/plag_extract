N, D = map(int, input().split())
X = []
for _ in range(N):
    line = list(map(int, input().split()))
    X.append(line)
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        dist2 = 0
        for k in range(D):
            dist2 += (X[i][k] - X[j][k])**2
        for l in range(200):
            if dist2 == l**2:
                ans += 1
                break
print(ans)
