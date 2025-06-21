from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
edge = []

for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)
    edge.append((a, b))

color = max([len(x) for x in graph])
print(color)

check = [False] * n
check[0] = True
DQ = deque()
DQ.append(0)

tree = [set() for i in range(n)]

while DQ:
    now = DQ.popleft()
    for node in graph[now]:
        if check[node] == False:
            check[node] = True
            tree[now].add(node)
            DQ.append(node)

memo = [False] * n
memo[0] = -1
DQ = deque()
DQ.append(0)

while DQ:
    now = DQ.popleft()
    if now == 0:
        c = 1
        for node in tree[now]:
            DQ.append(node)
            memo[node] = c
            c += 1
    else:
        c = 1
        for node in tree[now]:
            DQ.append(node)
            if c == memo[now]:
                c += 1
                memo[node] = c
                c += 1
            else:
                memo[node] = c
                c += 1

for a, b in edge:
    if a in tree[b]:
        print(memo[a])
    else:
        print(memo[b])