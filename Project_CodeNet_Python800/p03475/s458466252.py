n = int(input())
l = [list(map(int, input().split())) for _ in range(n-1)]


for i in range(n-1):
    t = 0
    for j in range(i, n-1):
        c = l[j][0]
        s = l[j][1]
        f = l[j][2]
        if t < s:
            t = s
        if t%f != 0:
            t = t+f - t%f
        t += c
    print(t)
print(0)