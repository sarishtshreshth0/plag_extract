N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N)]
cd = [tuple(map(int, input().split())) for _ in range(N)]

from operator import itemgetter
ab.sort(key=itemgetter(1))
cd.sort(key=itemgetter(0))

C = [0] * N
cnt = 0
for i in range(N):
    for j in range(N):
        if C[j] == 0 and ab[- j - 1][0] < cd[i][0] and ab[ - j - 1][1] < cd[i][1]:
            C[j] = 1
            cnt += 1
            break
print(cnt)
