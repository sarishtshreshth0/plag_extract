m,d = map(int, input().split())

ans = 0
for i in range(1,m+1):
    for d1 in range(2,10):
        if i % d1 == 0:
            d10 = i // d1
            if 2 <= d10 <= 9 and 10 * d10 + d1 <= d: ans += 1
print(ans)