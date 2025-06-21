from collections import deque
def main():
    # 入力
    n = int(input())
    nodes_edges_data = {e: [] for e in range(1, n + 1)}
    edges_data_to_number = {}
    for i1 in range(n - 1):
        a, b = tuple(map(int, input().split()))
        nodes_edges_data[a].append(b)
        nodes_edges_data[b].append(a)
        edges_data_to_number[(a, b)] = i1
        edges_data_to_number[(b, a)] = i1
    # 処理
    edges_color = [-1] * (n - 1)
    nodes_num = [0] * (n + 1)
    nodes_num[1] = -1
    max_edges_per_node = 0
    nodes_next = deque([1])
    nodes_next_next = deque()
    nodes_seen = set()
    while len(nodes_seen) < n:
        while nodes_next:
            e = nodes_next.pop()
            nodes_seen.add(e)
            adj_nodes = nodes_edges_data[e]
            nodes_next_next += adj_nodes
            num_of_nodes = len(adj_nodes)
            max_edges_per_node = max(max_edges_per_node, num_of_nodes)
            num = nodes_num[e]

            for adj_node in adj_nodes:
                if not adj_node in nodes_seen:

                    num = (num + 1) % max_edges_per_node
                    edges_color[edges_data_to_number[(e, adj_node)]] = num
                    #nodes_num[adj_node] = (num + 1) % max_edges_per_node
                    nodes_num[adj_node] = num
        nodes_next_next_set = set(nodes_next_next)
        nodes_next += deque(nodes_next_next_set - nodes_seen)
        nodes_next_next = deque()

    # 出力
    print(max(edges_color) + 1)
    for i in range(n - 1):
        print(edges_color[i] + 1)

if __name__ == '__main__':
    main()
