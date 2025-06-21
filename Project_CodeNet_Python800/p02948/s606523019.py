def main():
    import heapq
    n,m = map(int,input().split())
    alb = {}
    for i in range(n):
        a,b = map(int,input().split())
        if a not in alb.keys():
            alb[a] = [b]
        else:
            alb[a] += [b]
    h = []
    s = 0
    for i in range(1,m+1):
        if i in alb.keys():
            for j in range(len(alb[i])):
                heapq.heappush(h, -1*alb[i][j])
        if len(h)>0:
            m = heapq.heappop(h)
            s += -1*m
    print(s)

if __name__ == "__main__":
    main()