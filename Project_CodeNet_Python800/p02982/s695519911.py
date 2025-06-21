n, d = map(int, input().split())
x_l = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(i+1, n):
        tmp = 0
        for k in range(d):
            tmp += (x_l[j][k] - x_l[i][k]) ** 2
        if tmp**0.5%1 == 0:
            ans += 1

print(ans)
