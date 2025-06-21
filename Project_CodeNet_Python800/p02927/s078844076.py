M, D = map(int, input().split())

ans = 0

for m in range(1, M+1):
    for d in range(1, D+1):
        if d <= 21:
            pass
        else:
            d1, d10 = int(list(str(d))[1]), int(list(str(d))[0])
            if m == d1 * d10 and d1 > 1:
                ans += 1
                #print(m, d)
print(ans)