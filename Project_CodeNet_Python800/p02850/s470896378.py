def main():
    import sys
    readline = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    N = int(readline())
    R = [[int(i) for i in r.split()] for r in read().rstrip().split(b'\n')]
    G = [[] for _ in range(N)]
    edge = {}
    ans_key = []
    for a, b in R:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
        edge[(a-1, b-1)] = -1
        ans_key.append((a-1, b-1))
    max_g = max(len(g) for g in G)

    def dfs(max_g):
        todo = [0]
        seen = [False]*N
        seen[0] = True
        par = [-1]*N
        while todo:
            u = todo.pop()
            k = 0
            c = edge[(par[u], u)] if u != 0 else 0
            for v in G[u]:
                if seen[v]:
                    continue
                seen[v] = True
                todo.append(v)
                par[v] = u
                k += 1
                if k == c:
                    k += 1
                    if max_g < k:
                        k = 1
                if u < v:
                    edge[(u, v)] = k
                else:
                    edge[(v, u)] = k

    dfs(max_g)
    print(max_g)
    for k in ans_key:
        print(edge[k])


if __name__ == '__main__':
    main()
