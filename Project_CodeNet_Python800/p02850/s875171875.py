"""
参考    yy4さん 2019-11-24 21:24:43
516 ms          PyPy3 (2.4.0)
"""
#def solve():
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

connection = tuple(set() for _ in range(n))
for idx in range(n - 1):
    a, b = (int(x) - 1 for x in input().split())
    connection[a].add((b, idx))
    connection[b].add((a, idx))

q = deque()
q.append((0, -1, -1))

color_edge = [-1] * n  # color_edge[-1]は使わない
used = [False] * n
used[0] = True
while q:
    v, v_idx, prev_color = q.popleft()
    color_now = 1 if prev_color != 1 else 2
    for u, u_idx in connection[v]:
        if used[u]:
            continue
        used[u] = True
        color_edge[u_idx] = color_now
        q.append((u, u_idx, color_now))
        color_now += 1
        if color_now == prev_color:
            color_now += 1

ret = color_edge[:-1]
#return len(set(ret)), ret

    
#l, ret = solve()
l=len(set(ret))
print(l)
print(*ret, sep='\n')