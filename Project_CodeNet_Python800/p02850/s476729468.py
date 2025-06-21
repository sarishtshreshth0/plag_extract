def main():
    import sys
    sys.setrecursionlimit(10**5)
    N = int(input())
    G = [[] for _ in range(N)]
    edge = [-1] * (N-1)
    for i in range(N-1):
        a, b = (int(i)-1 for i in input().split())
        G[a].append((b, i))
        G[b].append((a, i))

    max_deg = max(len(G[i]) for i in range(N))

    def dfs(s, c=-1, p=-1):
        # 行きがけ順処理
        cur_color = 1
        for (v, i) in G[s]:
            if v == p:
                continue
            if c == cur_color:
                cur_color += 1
            edge[i] = cur_color
            dfs(v, edge[i], s)
            cur_color += 1
        # 帰りがけ順処理

    dfs(0)

    print(max_deg)
    for i in range(N-1):
        print(edge[i])


if __name__ == '__main__':
    main()
