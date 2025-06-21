N = int(input())
csf = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N-1):
    t = csf[i][1]
    t += csf[i][0]
    for j in range(i+1, N-1):
        st = csf[j][1]
        f = csf[j][2]
        t = max(st, ((t-1)//f+1)*f)
        t += csf[j][0]

    print(t)
print(0)


