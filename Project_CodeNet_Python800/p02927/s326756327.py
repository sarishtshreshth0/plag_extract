M, D = map(int, input().split())
cnt = 0
for m in range(1, M + 1):
    for dd in range(1, D + 1):
        if dd < 10:
            continue
        d1 = dd % 10
        d2 = (dd - d1) // 10
        if d1 > 1 and d2 > 1 and d1 * d2 == m:
            cnt += 1
print(cnt)