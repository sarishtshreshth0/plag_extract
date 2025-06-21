from collections import deque
n, m, k = map(int, input().split())
friend = [set() for _ in range(n + 1)]
block = [set() for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)
for i in range(k):
    a, b = map(int, input().split())
    block[a].add(b)
    block[b].add(a)
stack = deque()
ans = [0]*(n+1)
visited = [0]*(n+1)
for i in range(1, n+1):
    if visited[i]:
        continue
    link = {i}
    visited[i] = 1
    stack.append(i)
    while stack:
        n = stack.pop()
        for j in friend[n]:
            if visited[j] == 0:
                stack.append(j)
                visited[j] = 1
                link.add(j)
    for i in link:
        ans[i] = len(link) - len(link & friend[i]) - len(link & block[i]) -1
print(*ans[1:])