def main():
    N = int(input())
    G = [[] for _ in range(N)]
    edge = {}
    edge_order = [0]*(N-1)
    for i in range(N-1):
        a, b = (int(i)-1 for i in input().split())
        G[a].append(b)
        G[b].append(a)
        edge[a*N + b] = -1  # 辺(a,b)の色
        edge_order[i] = a*N + b
    # 辺彩色
    # 最大次数だけ色があればよさそう？
    # BFSで塗っていく
    # ある辺を塗るときに必要なのは，親の辺の色と，同じ親の頂点を持つ
    # 辺のうち彩色済みの色（陽に持たなくてよい）
    max_deg = max(len(G[i]) for i in range(N))

    from collections import deque

    def bfs(s):
        que = deque([])
        par = [-1]*N
        par_color = [-1]*N
        c = 0
        que.append(s)
        while que:
            pos = que.popleft()
            for v in G[pos]:
                if par[pos] == v:
                    continue
                if par_color[pos] == c:
                    c += 1
                    if c == max_deg:
                        c = 0
                if pos < v:
                    edge[pos * N + v] = c
                else:
                    edge[v * N + pos] = c
                par[v] = pos
                par_color[v] = c
                que.append(v)
                c += 1
                if c == max_deg:
                    c = 0

    bfs(0)

    print(max_deg)
    for i in range(N-1):
        print(edge[edge_order[i]] + 1)


if __name__ == '__main__':
    main()
