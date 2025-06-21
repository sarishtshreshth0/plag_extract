def f(u, i, d, t, vis):
    if vis[u]:
        return
    vis[u] = True
    z = t[u]

    c = 1
    for v in z:
        if vis[v]:
            continue
        if c == i:
            c += 1
        d[u].update({v: c})
        f(v, c, d, t, vis)
        c += 1


def main():
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(100000)
    n = int(input())
    t = [[] for _ in range(n + 1)]
    m = []

    for _ in range(n - 1):
        i, j = map(int, input().split())
        t[i].append(j)
        t[j].append(i)
        m.append([i, j])
    d = defaultdict(dict)
    vis = [False for _ in range(n + 1)]
    f(1, len(t[1]) + 1, d, t, vis)

    ans = ''
    if t.count([]) == n:
        ans += str(n - 1) + '\n'
    else:
        ans += str(max(len(i) for i in t)) + '\n'

    for (u, v) in m:
        ans += str(d[u][v]) + '\n'

    print(ans)


if __name__ == '__main__':
    main()
