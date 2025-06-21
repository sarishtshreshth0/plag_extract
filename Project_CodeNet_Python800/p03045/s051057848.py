N, M = map(int,input().split())
t = [[] for _ in range(N)]
visited = [0] * N
for _ in range(M):
    X, Y, Z = map(int,input().split())
    X -= 1
    Y -= 1
    t[X].append(Y)
    t[Y].append(X)
ans = 0
for i in range(N):
    if visited[i]:
        continue
    ans += 1
    stack = [i]
    while stack:
        s = stack.pop()
        for to in t[s]:
            if visited[to]:
                continue
            visited[to] = 1
            stack.append(to)
print(ans)