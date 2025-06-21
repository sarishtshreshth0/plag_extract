M, D = map(int, input().split())
ans = 0
for i in range(1, M + 1):
    for j in range(1, D + 1):
        d1, d10 = str(j).zfill(2)
        if int(d1) > 1 and int(d10) > 1 and i == int(d1) * int(d10):
            ans += 1
print(ans)
