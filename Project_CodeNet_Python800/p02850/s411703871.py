from collections import deque
n = int(input())
matrix= []
lis = [[] for i in range(n)]
ans = {}
for i in range(n):
    ans[i] = {}
for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    matrix.append(sorted([a,b]))
    lis[a].append(b)
    lis[b].append(a)
color = [-1 for _ in range(n)]
queue = deque([0])
color[0] = 1001001001
maxc = 0
while len(queue) > 0:
    now = queue.pop()
    used = color[now]
    tmp = 1
    for i in lis[now]:
        if color[i] == -1:
            queue.append(i)
            if tmp == used:
                tmp += 1
            color[i] = tmp
            ans[now][i] = tmp
            ans[i][now] = tmp
            maxc = max(maxc, tmp)
            tmp += 1
print(maxc)
for i in range(n-1):
    root = matrix[i]
    print(ans[root[0]][root[1]])