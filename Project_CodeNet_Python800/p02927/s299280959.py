m, d = map(int, input().split(' '))
ans = 0
for i in range(10, d + 1):
    s = str(i)
    d1 = int(s[1])
    d10 = int(s[0])
    if 2 <= d1 and 2 <= d10 and d1 * d10 <= m:
        ans += 1
print(ans)
