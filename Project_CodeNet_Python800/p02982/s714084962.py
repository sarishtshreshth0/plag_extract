N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        a = 0
        for l in range(D):
            a += (X[i][l] - X[j][l])**2
        a = a ** 0.5
        if a.is_integer():
            cnt += 1
        
print(cnt)