N, D = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        d = sum(abs(a[i][k] - a[j][k]) ** 2 for k in range(D)) ** 0.5
        cnt += d % 1 == 0
print(cnt)