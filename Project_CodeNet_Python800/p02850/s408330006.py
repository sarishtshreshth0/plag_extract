import sys
import numpy as np
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    edge = [[] for _ in range(N)]
    ab = [tuple() for _ in range(N - 1)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        edge[a].append(b)
        edge[b].append(a)
        ab[i] = (a, b)

    # print(ab)
    # print(edge)

    max_v = 0
    max_v_dim = 0
    for i, e in enumerate(edge):
        if max_v_dim < len(e):
            max_v_dim = len(e)
            max_v = i

    # print(max_v)
    # print(max_v_dim)

    # bfs
    q = deque()
    q.append(max_v)
    ec = np.full(N, -1, dtype='i8')
    ec[max_v] = max_v_dim + 10
    vc = dict()
    # vc = np.full((N, N), -1, dtype='i8')

    while q:
        nv = q.popleft()
        nc = ec[nv]
        tc = 1
        for v in edge[nv]:
            v1, v2 = min(nv, v), max(nv, v)
            if not ((v1, v2) in vc):
                if nc == tc:
                    tc += 1
                ec[v] = tc
                vc[(v1, v2)] = tc
                tc += 1
                q.append(v)

    print(max_v_dim)
    for v1, v2 in ab:
        print(vc[(v1, v2)])


if __name__ == '__main__':
    solve()
