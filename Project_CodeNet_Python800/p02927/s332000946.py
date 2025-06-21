m, d = map(int, input().split())

ans = 0
for i in range(22, d+1):
    d10 = i // 10
    d1 = i - d10 * 10
    if d10 > 1 and d1 > 1 and d10 * d1 <= m:
        ans += 1
print(ans)
