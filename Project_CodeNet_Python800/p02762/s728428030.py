from collections import deque

n, m, k = map(int, input().split())
friend = [set() for _ in range(n)]
block = [set() for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a - 1].add(b - 1)
    friend[b - 1].add(a - 1)
for _ in range(k):
    a, b = map(int, input().split())
    block[a - 1].add(b - 1)
    block[b - 1].add(a - 1)
visited = [0 for _ in range(n)]
ans = [None for _ in range(n)]
for i in range(n):
    if visited[i]:
        continue
    prefriends = {i}
    check = deque([i])
    while check:
        now = check.pop()
        visited[now] = 1
        for next in friend[now]:
            if visited[next] == 0:
                check.append(next)
                prefriends.add(next)
    for j in prefriends:
        ans[j] = len(prefriends) - 1 - len(friend[j]) - len(prefriends & block[j])
print(' '.join(list(map(str, ans)))) 