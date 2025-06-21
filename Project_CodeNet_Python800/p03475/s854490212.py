n = int(input())
L = [list(map(int, input().split())) for _ in range(n-1)]
for i in range(n-1):
    t = 0
    for j in range(i, n-1):
        if t <= L[j][1]:
            s = L[j][1]
        else:
            if t % L[j][2]:
                s = t + L[j][2] - (t % L[j][2])
            else:
                s = t
        t = s + L[j][0]
    print(t)
print(0)
