N = int(input())
ab = [list(map(int, input().split())) for i in range(N)]
cd = [list(map(int, input().split())) for i in range(N)]

ab.sort(key=lambda x:x[1])
cd.sort()
c = 0
for i in range(N):
    k = -1
    for j in range(len(ab)):
        if cd[i][0] > ab[j][0] and cd[i][1] > ab[j][1]:
            k = j
    if k != -1:
        c += 1
        ab = ab[:k] + ab[k + 1:]

print(c)