import sys

# import re
# import math
# import collections
# import decimal
# import bisect
# import itertools
# import fractions
# import functools
# import copy
# import heapq
# import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    edge = [[] for i in range(n)]
    origin_edge = []
    edge_dic = {}
    for i in range(n - 1):
        a, b = ns()
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
        edge_dic[(a, b)] = -1
        origin_edge.append((a, b))

    max_root = 0
    for e in edge:
        max_root = max(max_root, len(e))

    que = queue.Queue()
    que.put((0, -1))

    while que.qsize() > 0:
        node, used_color = que.get()
        current_color = 0 if used_color != 0 else 1
        for k in edge[node]:
            ai = min(node, k)
            bi = max(node, k)

            if edge_dic[(ai, bi)] > -1:
                continue

            edge_dic[(ai, bi)] = current_color
            que.put((k, current_color))
            current_color = current_color + 1 if used_color != current_color + 1 else current_color + 2

    print(max_root)
    for a, b in origin_edge:
        print(edge_dic[(a, b)] + 1)


if __name__ == '__main__':
    main()
