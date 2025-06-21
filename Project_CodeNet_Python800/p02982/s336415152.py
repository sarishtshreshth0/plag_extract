n, d = map(int, input().split())
p = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        dist = 0
        for k in range(d):
            dist += (p[i][k] - p[j][k])**2
        if int(dist**0.5) == dist**0.5:
            cnt += 1
print(cnt)