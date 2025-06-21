from collections import deque

N = int(input())
tree = [[] for i in range(N)]
edges = []

for i in range(N - 1):
    edges.append(tuple(map(int, input().split())))
    tree[edges[-1][0] - 1].append(edges[-1][1] - 1)
    tree[edges[-1][1] - 1].append(edges[-1][0] - 1)

coloring = {}
c_max = 1

color_used = [0]*N
v_dist = [-1]*N

queue = deque([0])
v_dist[0] = 0

while queue:
    v = queue.popleft()
    
    c = 1
    for n_v in tree[v]:
        if v_dist[n_v] < 0:
            v_dist[n_v] = v_dist[v] + 1

            if color_used[v] == c:
                c += 1
            
            coloring[(v, n_v)] = c
            coloring[(n_v, v)] = c
            color_used[n_v] = c
            queue.append(n_v)

            c += 1
    
    c_max = max(c_max, c)

print(c_max - 1)

for edge in edges:
    print(coloring[(edge[0]-1, edge[1]-1)])