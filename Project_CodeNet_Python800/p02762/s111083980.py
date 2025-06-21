def main():
    from sys import stdin
    input = stdin.readline

    n, m, k = map(int, input().split())
    f = [[] for i in range(n)]
    BL = [[] for i in range(n)]
    ans = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        f[a-1].append(b-1)
        f[b-1].append(a-1)
    for _ in range(k):
        c, d = map(int, input().split())
        BL[c-1].append(d-1)
        BL[d-1].append(c-1)
    D = {}
    parent = [-1] * n
    visited = [False] * n
    for root in range(n):
        if visited[root]:
            continue
        D[root]  = set([root])
        stack = [root]
        while stack:
            x = stack.pop()
            visited[x] = True
            parent[x] = root
            for t in f[x]:
                if visited[t]:
                    continue
                D[root].add(t)
                stack.append(t)
    for i in range(n):
        grp = D[parent[i]]
        tans = len(grp) - len(f[i]) - 1
        for block in BL[i]:
            if block in grp:
                tans -= 1
        ans[i] = tans
    print(*ans)
main()
