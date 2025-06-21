import collections
N = int(input())
edges = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append([b-1,i])
    edges[b-1].append([a-1,i])
# for i in edges:
#     print(i)
q = collections.deque()
q.append([0,-1,-1])
colors = [0]*(N-1)
check = [0]*N
while len(q) != 0:
    v, color, num = q.popleft()
    check[v] = 1
    # print(v,color,num)
    if colors[num] == 0 and color != -1:
        colors[num] = color
    next_color = 0
    for w in edges[v]:
        if check[w[0]] != 0:
            continue
        next_color += 1
        if next_color == colors[num]:
            next_color += 1
        q.append([w[0],next_color,w[1]])
# print(colors)
print(len(set(colors)))
for i in colors:
    print(i)