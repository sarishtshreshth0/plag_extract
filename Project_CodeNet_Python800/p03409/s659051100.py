n = int(input())
r = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]
r.sort(key=lambda x: x[1], reverse=True)
b.sort(key=lambda x: x[0])
ans = 0
for i, bb in enumerate(b):
    c, d = bb
    for j, rr in enumerate(r):
        a, b = rr
        if c > a and d > b:
            ans += 1
            del r[j]
            break
print(ans)
