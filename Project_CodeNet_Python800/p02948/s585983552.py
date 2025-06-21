def main():
    n,m = map(int,input().split())
    job =[[] for _ in range(m)]
    for i in range(n):
        a,b=map(int,input().split())
        if a-1 < m:
            job[a-1].append(-b) # b:asc, -b:desc
    
    res = 0
    q = []
    from heapq import heappop, heappush
    for i in range(m):
        for j in job[i]:
            heappush(q, j)
        if len(q) > 0:
            res += heappop(q) * -1 # -b -> b
    print(res)

if __name__ == '__main__':
    main()

