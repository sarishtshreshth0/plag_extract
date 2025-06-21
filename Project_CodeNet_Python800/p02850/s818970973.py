from collections import deque, Counter

N = int(input())

edge =  [[] for i in range(N-1)]
to = [[] for i in range(N)]
color = {}
edge_list = []

for i in range(N-1):
    a, b = map(int, input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)
    edge[i] = [a-1, b-1]
    edge_list.append(a-1)
    edge_list.append(b-1)

K = Counter(edge_list).most_common()[0][1]

q = deque([])
q.append([0,-1])

is_visited = [False] * N

while(len(q) != 0):
    cur_node, pre_col = q.popleft()

    is_visited[cur_node] = True
    col_use = 0

    for next_node in to[cur_node]:
        if not is_visited[next_node]:
            if col_use == pre_col:
                col_use += 1

            color[(cur_node,next_node)] = col_use
            q.append([next_node, col_use])
            col_use += 1

print(K)

for i in range(N-1):
    print(color[tuple(edge[i])] + 1)

