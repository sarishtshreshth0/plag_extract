# -*- coding: utf-8 -*-
"""
D - Coloring Edges on Tree
https://atcoder.jp/contests/abc146/tasks/abc146_d

"""
import sys


from collections import OrderedDict, deque

def main(args):
    N = int(input())
    G = [[] for _ in range(N+1)]
    res = OrderedDict()
    for _ in range(N-1):
        a, b = map(int, input().split())
        res[(a, b)] = -1
        G[a].append(b)
        G[b].append(a)

    k = max(len(g) for g in G)
    colors = [0 for _ in range(N+1)]
    q = deque([1])
    visited = set([1])
    while q:
        cn = q.popleft()
        color = 1
        for nn in G[cn]:
            if nn not in visited:
                if color == colors[cn]:
                    color += 1
                visited.add(nn)
                q.append(nn)
                c = color
                colors[nn] = color
                color += 1
                if (cn, nn) in res:
                    res[(cn, nn)] = c
                if (nn, cn) in res:
                    res[(nn, cn)] = c
    print(k)
    for v in res.values():
        print(v)


if __name__ == '__main__':
    main(sys.argv[1:])
