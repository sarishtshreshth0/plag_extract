n,d = map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if i == j: continue
        counter = 0
        for k in range(d):
            diff = abs(x[i][k] - x[j][k])
            counter += diff ** 2
        ok = False
        for k in range(10000):
            if k * k == counter: ok = True
        if ok: ans += 1
print(ans // 2)