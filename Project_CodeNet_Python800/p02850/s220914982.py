def resolve():
    N = int(input())
    g = {}
    for i in range(N-1):
        a, b = list(map(int, input().split()))
        g.setdefault(a-1, [])
        g[a-1].append((b-1, i))
        g.setdefault(b-1, [])
        g[b-1].append((a-1, i))
        
    nodes = [(None, 0)]
    colors = [None for _ in range(N-1)]
    maxdeg = 0
    while nodes:
        prevcol, node = nodes.pop()
        maxdeg = max(maxdeg, len(g[node]))
        color = 1 if prevcol != 1 else 2
        for nxt, colidx in g[node]:
            if colors[colidx] is None:
                colors[colidx] = color
                nodes.append((color, nxt))
                color += 1 if prevcol != color+1 else 2

    print(maxdeg)
    for col in colors:
        print(col)
            



if '__main__' == __name__:
    resolve()
