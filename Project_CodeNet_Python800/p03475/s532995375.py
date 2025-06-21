N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N - 1)]
for i in range(N):
    t = 0
    for c, s, f in CSF[i:]:
        if t > s:
            if t % f:
                t += f - t % f
        else:
            t = s
        t += c
    print(t)
