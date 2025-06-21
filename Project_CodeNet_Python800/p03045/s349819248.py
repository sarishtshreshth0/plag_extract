from collections import deque

N, M = map(int, input().split())
a = [-1 for _ in range(N)]
visited = [0 for _ in range(N)]
cond = [[[],[]] for _ in range(N)]#same,diff
count = 0
for _ in range(M):
    x, y, z = map(int, input().split())
    if z % 2 == 0:
        cond[x-1][0].append(y-1)
        cond[y-1][0].append(x-1)
    else:
        cond[x-1][1].append(y-1)
        cond[y-1][1].append(x-1)
for i in range(N):
    if (not cond[i][0] and not cond[i][1]) or visited[i]:
        continue
    else:
        count += 1
        check = deque([(i, 0)])
        while check:
            num, eo = check.popleft()
            visited[num] = 1
            a[num] = eo
            for next in cond[num][0]:
                if visited[next]:
                    continue
                check.append((next, eo))
            for next in cond[num][1]:
                if visited[next]:
                    continue
                check.append((next, (eo+1)%2))
ans = a.count(-1) + count
print(ans)