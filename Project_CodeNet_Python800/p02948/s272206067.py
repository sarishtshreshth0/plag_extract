def main():
    import heapq
    n, m, *ab = map(int, open(0).read().split())
    l = [[] for _ in range(m + 1)]
    for i, j in zip(*[iter(ab)] * 2):
        if i <= m:
            heapq.heappush(l[i], -j)
    
    ans = 0
    h = []
    for i in range(1, m + 1):
        for j in l[i]:
            heapq.heappush(h, j)
        if len(h) > 0:
            x = heapq.heappop(h)
            ans += x

    print(-ans)


if __name__ == '__main__':
    main()
