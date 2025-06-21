def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())

    g = tuple(set() for _ in range(N))
    for _ in range(M):
        x, y, _ = (int(x) - 1 for x in input().split())
        g[x].add(y)
        g[y].add(x)

    ans = 0
    checked = [False] * N
    for s in range(N):
        if checked[s]: continue
        checked[s] = True
        ans += 1

        dq = deque([s])
        while dq:
            v = dq.popleft()
            for u in g[v]:
                if checked[u]: continue
                checked[u] = True
                dq.append(u)

    print(ans)


if __name__ == '__main__':
    main()
