M, D = map(int, input().split())
if D < 10:
    print(0)
    exit()
ans = 0
for m in range(1, M+1):
    for d in range(10, D+1):
        d10, d1 = map(int, (str(d)[1], str(d)[0]))
        if d10 >= 2 and d1 >= 2 and d10*d1 == m:
            ans += 1

print(ans)
