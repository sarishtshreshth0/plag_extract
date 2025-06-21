n = int(input())
l = [[0]*3 for i in range(n)]

for i in range(n - 1):
    c, s, f = map(int, input().split())
    l[i][0] = c
    l[i][1] = s
    l[i][2] = f

for i in range(n - 1):
    t = 0
    for j in range(i, n - 1):
        t = max(l[j][1], t)
        mod = abs(t - l[j][1])%l[j][2]
        if mod != 0:
            t += l[j][2] - mod
        t += l[j][0]
    print(t)

print(0)