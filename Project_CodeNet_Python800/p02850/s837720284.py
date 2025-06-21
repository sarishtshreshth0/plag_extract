import collections

n = int(input())
graph = [[] for i in range(n + 1)]
edge = []
for i in range(n - 1):
    a, b = map(int, input().split())
    edge.append((a, b))
    graph[a].append(b)
    graph[b].append(a)
color = {}
queue = collections.deque([(1, 0)])
while queue:
    temp = queue.popleft()
    num = temp[0]
    prev = temp[1]
    if prev:
        col = color[(prev, num)]
    else:
        col = 0
    count = 1
    for i in graph[num]:
        a, b = min(i, num), max(i, num)
        if (a, b) in color.keys():
            continue
        else:
            if count == col:
                color[(a, b)] = count + 1
                count += 2
            else:
                color[(a, b)] = count
                count += 1
            queue.append((i, num))
print(max([len(graph[i]) for i in range(n + 1)]))
for i, j in edge:
    print(color[(i, j)])