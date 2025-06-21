def main():
    from heapq import heappush as sushi
    from heapq import heappop as tempra
    n, m, *ab = map(int, open(0).read().split())
    l = [[] for _ in range(m + 1)]
    for i, j in zip(*[iter(ab)] * 2):
        if i - m < 1:
            l[i].append(-j)

    w = []
    h = []
    for i in range(1, m + 1):
        for j in l[i]:
            sushi(h, j)
        if h:
            x = tempra(h)
            w.append(x)

    print(-sum(w))


if __name__ == '__main__':
    main()
