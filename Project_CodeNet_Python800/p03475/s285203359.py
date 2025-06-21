n = int(input())
l = [list(map(int, input().split())) for i in range(n - 1)]

for i in range(n):
    t = 0
    for c, s, f in l[i:]:
        t = max(s, t)
        mod = abs(t - s)%f
        if mod != 0:
            t += f - mod
        t += c
    print(t)