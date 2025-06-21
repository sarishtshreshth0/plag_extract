N, D = map(int, input().split())
X = [input().split() for _ in range(N)]

res = 0
for i in range(N - 1):
    for k in range(i + 1, N):
        ans = 0.0
        for j in range(D):
            ans += abs( (int(X[i][j]) - int(X[k][j]))**2 )
    
        ans = ans ** (1/2)
        if ans.is_integer():
            res += 1

print(res)