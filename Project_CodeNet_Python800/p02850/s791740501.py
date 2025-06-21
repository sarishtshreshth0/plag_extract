def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N = int(input())

    g = tuple(set() for _ in range(N))
    for i in range(N - 1):
        a, b = (int(x) - 1 for x in input().split())
        g[a].add((b, i))
        g[b].add((a, i))

    dq = deque()
    dq.append([0, -1])
    color = [-1] * (N - 1)
    while dq:
        v, skip = dq.popleft()
        color_to_use = 1
        for u, i in g[v]:
            if ~color[i]: continue
            if color_to_use == skip:
                color_to_use += 1
            color[i] = color_to_use
            dq.append((u, color_to_use))
            color_to_use += 1

    print(max(color))
    print(*color, sep='\n')


if __name__ == '__main__':
    main()
