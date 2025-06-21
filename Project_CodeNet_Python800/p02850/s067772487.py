def main():
    N = int(input())
    G = [[] for _ in range(N)]
    edge = [-1] * (N-1)
    for i in range(N-1):
        a, b = (int(i)-1 for i in input().split())
        G[a].append(b*N + i)
        G[b].append(a*N + i)

    max_deg = max(len(G[i]) for i in range(N))

    from collections import deque

    def bfs(s):
        que = deque([])
        par = [-1]*N
        que.append(s)
        while que:
            pos = que.popleft()
            c = -1
            k = 1
            for vi in G[pos]:
                v, i = divmod(vi, N)
                if par[pos] == v:
                    c = edge[i]
            for vi in G[pos]:
                v, i = divmod(vi, N)
                if par[pos] == v:
                    continue
                if k == c:
                    k += 1
                par[v] = pos
                edge[i] = k
                k += 1
                que.append(v)

    bfs(0)

    print(max_deg)
    for i in range(N-1):
        print(edge[i])


if __name__ == '__main__':
    main()
