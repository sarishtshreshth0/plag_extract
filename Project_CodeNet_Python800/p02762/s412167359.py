from collections import deque

n, m, k = map(int, input().split())

#listを組むより早い
friends = [set() for _ in range(n)]
blocks = [set() for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    friends[a-1].add(b-1)
    friends[b-1].add(a-1)

for i in range(k):
    c, d = map(int, input().split())
    blocks[c-1].add(d-1)
    blocks[d-1].add(c-1)

q = deque()
ans = [0] * n
visited = [0] * n

for i in range(n):
    if visited[i]:
        continue
    #集合を構築していく
    group = {i}
    visited[i] = 1
    q.append(i)
    while q:
        k = q.popleft()
        for j in friends[k]:
            if not visited[j]:
                q.append(j)
                group.add(j)
                visited[j] = 1
    
    # できた集合内でとりあえず計算
    for l in group:
        ans[l] = len(group) - len(blocks[l] & group) - len(friends[l] & group) - 1
print(*ans)
#print(*ans,sep="\n")