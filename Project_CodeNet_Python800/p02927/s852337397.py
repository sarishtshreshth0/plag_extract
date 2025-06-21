M,D = map(int,input().split())

ans = 0
for m in range(4,M+1):
    for d in range(22,D+1):
        d = str(d)
        da = d[0]
        db = d[1]
        if int(db) < 2:continue
        if m == int(da)*int(db):
            ans += 1
print(ans)