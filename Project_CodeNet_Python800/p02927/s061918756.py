m, d = map(int, input().split())

ans = 0
for mi in range(1, m + 1):
    for di in range(1, d + 1):
        d10, d1 = divmod(di, 10)
        if d1 >= 2 and d10 >= 2 and mi == d10 * d1:
            ans += 1

print(ans)
