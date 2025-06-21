n = int(input())
rlst = []
blst = []

for _ in range(n):
    w, h = map(int, input().split())
    rlst.append([w, h, 0])
for _ in range(n):
    w, h = map(int, input().split())
    blst.append([w, h, 0])
    
rlst = sorted(rlst, key=lambda x:(x[1],x[0]))
blst = sorted(blst, key=lambda x:(x[0],x[1]))

ans = 0
for b in blst:
    i = 0
    for r in rlst:
        if r[0] < b[0] and r[1] < b[1] and r[2] == 0:
            ridx = i
            b[2] = 1
        i += 1
    if b[2] == 1:
        ans += 1
        rlst[ridx][2] = 1
print(ans)