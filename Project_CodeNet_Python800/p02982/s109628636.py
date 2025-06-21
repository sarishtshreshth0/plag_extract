N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        sum = 0.0
        if i != j:
            for k in range(len(X[i])):
                sum += (X[i][k] - X[j][k])**2
        sum = sum**0.5
        if sum.is_integer() and sum!=0.0:
            cnt += 1
print(cnt//2)