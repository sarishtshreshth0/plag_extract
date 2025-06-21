n, d = map(int, input().split())

x = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        count = 0
        for y in range(d):
            count += abs(x[i][y]-x[j][y])**2

        if (count**0.5) % 1 == 0:
            ans += 1

print(ans)
