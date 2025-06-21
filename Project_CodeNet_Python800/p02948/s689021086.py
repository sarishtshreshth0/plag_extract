def main():
    import heapq
    n,m = map(int,input().split())
    job = {}
    for i in range(n):
        a,b = map(int,input().split())
        if a not in job.keys():
            job[a] = [b]
        else:
            job[a].append(b)
    ans = 0
    hp = []
    for i in range(1,m+1):
        if i in job.keys():
            for j in range(len(job[i])):
                heapq.heappush(hp,-1*job[i][j])
        if len(hp)>0:
            ans += -1*heapq.heappop(hp)
    print(ans)

if __name__ == "__main__":
    main()
