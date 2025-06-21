n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        norm = 0
        for k in range(d):
            diff = abs(x[i][k] - x[j][k])
            norm += diff ** 2

        flag = False
        for k in range(norm+1):
            if k ** 2 == norm:
                flag = True
        if flag:
            ans += 1

print(ans)
