def main():
    import heapq
    n,m = map(int,input().split())
    A = {}
    for i in range(n):
        a,b = map(int,input().split())
        if a not in A.keys():
            A[a] = [b]
        else:
            A[a].append(b)
    J = []
    ans = 0
    for i in range(1,m+1):
        if A.get(i)!=None:
            for k in A[i]:
                heapq.heappush(J,-1*k)
        if len(J)>0:
            ans += -1* heapq.heappop(J)
    print(ans)

if __name__ == "__main__":
    main()
