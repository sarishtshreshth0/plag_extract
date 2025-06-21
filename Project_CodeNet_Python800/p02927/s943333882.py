M, D = [int(_) for _ in input().split()]

ans = 0
for m in range(1, M+1):
    for d in range(1, D+1):
        d10 = d // 10
        d1 = d % 10
        if d10 < 2 or d1 < 2:
            continue
        if d1 * d10 == m:
            ans += 1
print(ans)
