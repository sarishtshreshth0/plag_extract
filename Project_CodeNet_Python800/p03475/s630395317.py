n = int(input())
csf = [list(map(int, input().split())) for _ in range(n - 1)]

for i in range(n):
    t = 0
    for j in range(i, n - 1):
        if t < csf[j][1]:
            t = csf[j][1]
        else:
            if t % csf[j][2] != 0:
                t = (t // csf[j][2] + 1) * csf[j][2]
        t += csf[j][0]
    print(t)