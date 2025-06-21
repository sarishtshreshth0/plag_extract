n = int(input())
stations = []
for _ in range(n-1):
    stations.append(tuple(map(int, input().split())))

outputs = [0] * n
for i in range(n-1):
    t = 0
    for j in range(i, n-1):
        c, s, f = stations[j]
        if t <= s:
            t = s
        else:
            if t%f != 0:
                t = t+f - t%f
        t += c
    print(t)
print(0)
