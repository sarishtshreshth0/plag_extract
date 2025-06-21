N = int(input())

stations = [tuple(map(int, input().split(' '))) for _ in range(N - 1)]

for i in range(N - 1):
    t = 0
    for j in range(i, N - 1):
        c, s, f = stations[j]
        t = max(t, s)
        if t % f != 0:
            t += f - t % f
        t += c
    print(t)
print(0)
