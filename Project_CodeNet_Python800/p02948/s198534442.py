#137D
def main():
    import sys
    import heapq as h
    from collections import defaultdict
    N, M = map(int, sys.stdin.readline().split())
    L = tuple([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])
    #print(L)
    D = defaultdict(list)
    for i in range(N):
        D[L[i][0]-1].append(-L[i][1])
    
    #print(D)
    ans = 0
    tmp=[]
    h.heapify(tmp)
    for d in range(M):
        for b in D[d]:
            h.heappush(tmp, b)
        #print(tmp)
        if tmp:
            ans += h.heappop(tmp)
        
    print(-ans)



if __name__=='__main__':
    main()