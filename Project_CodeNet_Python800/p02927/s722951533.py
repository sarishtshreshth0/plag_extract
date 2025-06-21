m, d = map(int, input().split())
ans = 0
for i in range(22,d+1):
    d0, d1 = int(str(i)[0]), int(str(i)[1])
    if d0 < 2 or d1 < 2: continue
    if 1 <= d0*d1 <= m: ans += 1
print(ans)