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

    queue = deque([0])
    color = [0] * (N - 1)
    color_from_parent = [0] * N
    color_from_parent[0] = -1

    while queue:
        v = queue.popleft()
        c = 1
        for i, nv in G[v]:
            if color_from_parent[nv] != 0:
                continue
            if c == color_from_parent[v]:
                c += 1
            color_from_parent[nv] = c
            color[i] = c
            c += 1
            queue.append(nv)

    print(max(color))
    print(*color, sep='\n')
    return


if __name__ == '__main__':
    main()
