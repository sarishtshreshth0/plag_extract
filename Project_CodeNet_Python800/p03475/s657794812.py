n = int(input())
stations = [list(map(int, input().split())) for _ in range(n-1)]
for idx in range(n-1):
    t = 0
    for idx2 in range(idx, n-1):
        c, s, f = stations[idx2]
        t = max(t, s)
        if t <= f:
            t = f
        else:
            if t%f > 0:
                t += f - t%f
        t += c
    print(t)
print(0)