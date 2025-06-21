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
    for i, (a, b) in enumerate(zip(*[iter(AB)] * 2)):
        G[a - 1].append((i, b - 1))
        G[b - 1].append((i, a - 1))

    color = [0] * (N - 1)

    def dfs(v, p, pc):
        c = 1
        for i, nv in G[v]:
            if nv == p:
                continue
            if c == pc:
                c += 1
            color[i] = c
            dfs(nv, v, c)
            c += 1

    dfs(0, -1, 0)

    print(max(color))
    print('\n'.join(map(str, color)))
    return


if __name__ == '__main__':
    main()
