n, D = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        cnt = 0
        for d in range(D):
            cnt += (x[i][d] - x[j][d])**2
        if (cnt**0.5).is_integer():
            ans += 1
print(ans)