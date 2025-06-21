N, D = map(int,input().split())

X = []
for _ in range(N):
    X_i = list(map(int,input().split()))
    X.append(X_i)

ans = 0
for i in range(N):
    for j in range(i+1,N):
        dist = 0
        for d in range(D):
            dist += (X[i][d] - X[j][d]) ** 2

        for k in range(1000):
            if dist == k**2:
                ans += 1

print(ans)
        
