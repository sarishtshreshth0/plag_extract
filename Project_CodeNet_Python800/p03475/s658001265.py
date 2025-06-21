n = int(input())
CSF = [tuple(map(int, input().split())) for _ in range(n - 1)]

for i in range(n):
    t = 0
    for c, s, f in CSF[i:]:
        if t < s:
            t = s
        elif t % f != 0:
            t += f - t % f
        t += c
    print(t)
