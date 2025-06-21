import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *AB = map(int, read().split())
    G = [[] for _ in range(N)]

    for a, b in zip(*[iter(AB)] * 2):
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    queue = deque([0])
    parent = [-1] * N
    order = []

    while queue:
        v = queue.popleft()
        order.append(v)
        for nv in G[v]:
            if nv == parent[v]:
                continue
            parent[nv] = v
            queue.append(nv)

    color = [0] * N
    for v in order:
        c = 1
        for nv in G[v]:
            if nv == parent[v]:
                continue
            if c == color[v]:
                c += 1
            color[nv] = c
            c += 1

    ans = [0] * (N - 1)
    for i, (a, b) in enumerate(zip(*[iter(AB)] * 2)):
        if parent[a - 1] == b - 1:
            ans[i] = color[a - 1]
        else:
            ans[i] = color[b - 1]

    print(max(ans))
    print(*ans, sep='\n')
    return


if __name__ == '__main__':
    main()
