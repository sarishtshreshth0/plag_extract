m, d = map(int, input().split())

ans = 0
for em in range(1, m + 1):
    for ed in range(1, d + 1):
        q, r = divmod(ed, 10)
        if q >= 2 and r >= 2 and q * r == em:
            ans += 1

print(ans)
