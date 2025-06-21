n = int(input())

csf = []

for i in range(n - 1):
    c, s, f = map(int, input().split())
    csf.append([c, s, f])

ans = []
for i in range(n - 1):
    tmp = csf[i][0] + csf[i][1]
    for j in range(i + 1, n - 1):
        if tmp < csf[j][1]:
            tmp = csf[j][0] + csf[j][1]
        elif (tmp - csf[j][1]) % csf[j][2] == 0:
            tmp += csf[j][0]
        else:
            tmp = (tmp // csf[j][2] + 1) * csf[j][2] + csf[j][0]
    ans.append(tmp)
ans.append(0)

print(*ans, sep="\n")