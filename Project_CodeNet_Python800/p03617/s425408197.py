l = [[0.25],[0.5],[1],[2]]
tmp = list(map(int,input().split()))

for i in range(4):
    l[i].append(tmp[i])

for i in range(4):
    l[i].append(l[i][1]*4/(l[i][0]*4))

from operator import itemgetter
l = sorted(l, key=itemgetter(2))

ans = 0
n = 4*int(input())
for i in range(4):
    tmp = n//int(l[i][0]*4)
    if tmp >= 1:
        ans += tmp * l[i][1]
        n -= tmp*int(l[i][0]*4)

print(int(ans))
