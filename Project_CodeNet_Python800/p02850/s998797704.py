from collections import defaultdict, deque


def main():
    N = int(input())
    edges = list()
    adj_nodes = defaultdict(list)
    for _ in range(N - 1):
        a, b = list(map(int, input().split(' ')))
        a -= 1
        b -= 1
        edges.append((a, b))
        adj_nodes[a].append(b)
        adj_nodes[b].append(a)
    MAX_COLORS = max([len(nodes) for nodes in adj_nodes.values()])
    # BFS
    edge_colors = dict()
    frontier = deque()
    frontier.append((None, 0, None))  # from_node, to_node, color
    explored = [0 for _ in range(N)]
    while len(frontier) > 0:
        n = frontier.popleft()
        explored[n[1]] = 1
        next_from_node = n[1]
        before_color = n[2] if n[2] is not None else (MAX_COLORS - 1)
        next_color = before_color
        next_to_nodes = adj_nodes[next_from_node]
        for next_to_node in next_to_nodes:
            if explored[next_to_node] == 1:
                continue
            next_color = (next_color + 1) % MAX_COLORS
            frontier.append((next_from_node, next_to_node, next_color))
            edge_colors[(next_from_node, next_to_node)] = next_color
            edge_colors[(next_to_node, next_from_node)] = next_color
    # print answer
    print(MAX_COLORS)
    for edge in edges:
        print(edge_colors[edge] + 1)


if __name__ == '__main__':
    main()