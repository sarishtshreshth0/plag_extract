import heapq

n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort(key = lambda x : x[0])
q = []
heapq.heapify(q)
ind = 0
ans = 0
for i in range(1,m+1):
    ok = True
    while ok:
        if  ind <= n-1 and ab[ind][0] <= i:
            heapq.heappush(q, -1 * ab[ind][1])
            ind += 1
        else:
            ok = False
    if len(q) >= 1:
        ans -= heapq.heappop(q)
print(ans)
