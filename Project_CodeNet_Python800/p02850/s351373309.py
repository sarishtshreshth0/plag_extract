import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
adj = [[] for _ in range(N)]
degrees = [0 for _ in range(N)]
edges = {}
for i in range(N - 1):
    a, b = map(int, input().split()) 
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)
    degrees[a] += 1
    degrees[b] += 1
    edges[(a, b)] = i

max_degree = max(degrees)
print(max_degree)

edge_colors = [-1 for _ in range(N - 1)]
visited = [False for _ in range(N)]

def dfs(v, color):
    global max_degree
    if visited[v]:
        return
    visited[v] = True

    next_color = color + 1
    next_color %= max_degree
    for u in adj[v]:
        if visited[u]:
            continue
        if u < v:
            edge_colors[edges[(u, v)]] = next_color
        else:
            edge_colors[edges[(v, u)]] = next_color

        dfs(u, next_color)
        next_color += 1
        # if color == next_color:
        next_color %= max_degree

dfs(0, -1)
for i in range(N - 1):
    print(edge_colors[i] + 1)