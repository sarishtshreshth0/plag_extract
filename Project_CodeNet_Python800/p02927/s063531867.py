m, d = map(int, input().split())

ans = 0
for i in range(1, m+1):
    for j in range(1, d+1):
        d1 = j % 10
        d2 = (j - d1) // 10
        if (d1 > 1) and (d2 > 1):
            if d1 * d2 == i:
                ans += 1

print(ans)