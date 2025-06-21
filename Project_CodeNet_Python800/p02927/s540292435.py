M, D = map(int, input().split())
ans = 0
for m in range(1, M+1):
    for d in range(1, D+1):
        if d <= 9:
            continue
        d = str(d)
        d1 = int(d[0])
        d2 = int(d[1])
        if d1 >= 2 and d2 >= 2 and m == d1*d2:
            #print(m, d1, d2)
            ans += 1
print(ans)
