import copy
n = int(input())
c = [list(map(int, input().split())) for i in range(n-1)]
for i in range(n):
    t = 0
    for j in range(i, n-1):
        if t < c[j][1]:
            t = c[j][1]
        elif t%c[j][2] == 0:
            pass
        else:
            t += c[j][2] - t%c[j][2]
        t += c[j][0]
    print(t)