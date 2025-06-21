def resolve():
    N = int(input())
    g = {}
    edges_to_idx = {}
    edges = []
    for i in range(N-1):
        a, b = list(map(int, input().split()))
        g.setdefault(a-1, [])
        g[a-1].append(b-1)
        g.setdefault(b-1, [])
        g[b-1].append(a-1)
        edges_to_idx.setdefault("{}-{}".format(a-1, b-1), i)
        edges_to_idx.setdefault("{}-{}".format(b-1, a-1), i)
        edges.append((a-1, b-1))

    nodes = [(None, 0)]
    colors = [None for _ in range(N-1)]
    maxdeg = 0
    while nodes:
        prevcol, node = nodes.pop()
        maxdeg = max(maxdeg, len(g[node]))
        idx = 0
        for col in range(1, len(g[node])+1):
            if col == prevcol:
                continue
            nxt = g[node][idx]
            coloridx = edges_to_idx["{}-{}".format(node, nxt)] 
            if colors[coloridx] is not None:
                idx += 1
                if idx >= len(g[node]):
                    break
                nxt = g[node][idx]
                coloridx = edges_to_idx["{}-{}".format(node, nxt)] 
            colors[coloridx] = col
            nodes.append((col, nxt))
            idx += 1
            if idx >= len(g[node]):
                break
            
    
    print(maxdeg)
    for col in colors:
        print(col)
            
            




if '__main__' == __name__:
    resolve()
