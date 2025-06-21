import sys
sys.setrecursionlimit(10 ** 9)

# 昔同じ問題を atcoder で見た？
n = int(input())
edges = []
paths = {}
for i in range(n-1):
    a, b = list(map(int, input().split(' ')))
    edges.append((a, b))
    paths[a] = paths.get(a, []) + [b]
    paths[b] = paths.get(b, []) + [a]
# print(edges)
# print(paths)
colors = {}  # (a->b) 1 とか
current = 1
biggest = 1
def f(current, prev, prev_color):
    global biggest
    color = 0
    for vertex in paths[current]:
        if vertex == prev:
            continue
        color += 1
        if color == prev_color:
            color += 1
        biggest = max(biggest, color)
        colors[(current, vertex)] = color
        f(vertex, current, color)
f(1, None, None)

print(biggest)
for a, b in edges:
    print(colors[(a, b)])
# pypy3