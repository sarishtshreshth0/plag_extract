def resolve():
    N, M = list(map(int, input().split()))
    AB = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    #print(AB)
    import heapq
    cands = []
    abidx = 0
    ans = 0
    day = M
    while day > 0:
        #print(abidx)
        while abidx < N and AB[abidx][0] <= M-day+1:
            _, point = AB[abidx]
            heapq.heappush(cands, -point)
            abidx += 1
        if len(cands) > 0:
            ans += heapq.heappop(cands)
            #print(-ans)
        day -= 1
    print(-ans)


if '__main__' == __name__:
    resolve()