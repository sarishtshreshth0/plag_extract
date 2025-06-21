from collections import deque
N = int(input())
adj = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    adj[a-1].append((b, i))
    adj[b-1].append((a, i))
# print(adj)
color = [0]*N
visited = [False]*N
visited[0] = True
queue = deque([1])
ans = [0]*(N-1)
while queue:
    now = queue.popleft()
    cnt = 1
    for n, e in adj[now-1]:
        if visited[n-1]:
            continue
        if color[now-1] == cnt:
            cnt += 1
        color[n-1] = cnt
        visited[n-1] = True
        ans[e] = cnt
        cnt += 1
        queue.append(n)
print(max(color))
print(*ans, sep='\n')