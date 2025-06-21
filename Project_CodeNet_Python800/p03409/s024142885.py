n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]
cd = [list(map(int,input().split())) for i in range(n)]
ab = sorted(ab, key = lambda x:x[1], reverse=True)
cd = sorted(cd)
log = [0] * n
cnt = 0
for i in range(n):
    c, d = cd[i]
    for j in range(n):
        if log[j]:continue
        a, b = ab[j]
        if a < c and b < d:
            cnt += 1
            log[j] = 1
            break
print(cnt)