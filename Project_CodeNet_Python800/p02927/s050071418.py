M, D = map(int, input().split())

ans = 0
for m in range(1, M + 1):
    for d in range(10, D + 1):
        d1 = int(str(d)[0])
        d2 = int(str(d)[1])
        if m == d1 * d2 and d1 > 1 and d2 > 1:
            ans += 1

print(ans)
