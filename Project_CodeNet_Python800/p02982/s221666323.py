n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        num = 0
        for k in range(d):
            num += (x[i][k] - x[j][k])**2
        for l in range(200):
            if num == l**2:
                ans += 1
print(ans)