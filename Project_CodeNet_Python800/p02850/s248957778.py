from collections import deque
import sys
sys.setrecursionlimit(10**9)


N = int(input())
to = [[] for _ in range(N)]
order = []

for _ in range(N - 1):
    a, b = list(map(lambda x:int(x) - 1, input().split()))
    to[a].append(b)
    to[b].append(a)
    order.append(b)


def solve():
    dist = [-1] * N
    # 頂点iに向かう辺をiとする
    color = [0] * N
    dist[0] = 0
    color[0] = 0
    que = deque([0])

    while que:
        v = que.popleft()
        used_color = [color[v]]
        next_color = 1
        for nv in to[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                while next_color in used_color:
                    next_color += 1
                color[nv] = next_color
                used_color.append(next_color)
                que.append(nv)

    print(len(set(color[1:])))
    for i in range(N - 1):
        print(color[order[i]])


if __name__ == "__main__":
    solve()
