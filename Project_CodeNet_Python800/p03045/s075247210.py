import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    tree = [[] for _ in range(n)]
    for _ in range(m):
        x, y, _ = map(int, input().split())
        tree[x - 1].append(y - 1)
        tree[y - 1].append(x - 1)

    def dfs(v):
        for u in tree[v]:
            if visited[u]:
                continue
            else:
                visited[u] = True
                dfs(u)

    visited = [False for _ in range(n)]
    res = 0
    for i in range(n):
        if not visited[i]:
            res += 1
            visited[i] = True
            dfs(i)

    print(res)


if __name__ == '__main__':
    resolve()
