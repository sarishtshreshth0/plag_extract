import sys
input = sys.stdin.readline

n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
cd = [list(map(int,input().split())) for _ in range(n)]

ans = 0
used = [False]*n
ab.sort(key = lambda x: x[1])
ab.sort(key = lambda x: x[0])
cd.sort(key = lambda x: x[1])
cd.sort(key = lambda x: x[0])

for i in range(n):
    c,d = cd[i]
    li = []
    for j in range(n):
        if ab[j][0] < c and ab[j][1] < d and not used[j]:
            li.append((ab[j], j))
    max_idx = 0
    max_tmp = -1
    if li:
        for j in li:
            if max_tmp < j[0][1]:
                max_tmp = j[0][1]
                max_idx = j[1]
        ans += 1
        used[max_idx] = True

print(ans)
