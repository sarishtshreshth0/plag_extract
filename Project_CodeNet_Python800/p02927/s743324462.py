m, d = map(int, input().split())
ans = 0
for i in range(2, d + 1):
    d1 = i % 10
    d10 = i // 10 % 10
    if d1 <= 1 or d10 <= 1:
        continue
    if d1 * d10 in range(2, m + 1):
        ans += 1

print(ans)
