import heapq
n,m=map(int,input().split())
x=sorted(list(map(int,input().split())))
diff=[]
heapq.heapify(diff)
if n>=m:
    print(0)
else:
    for i in range(m-1):
        heapq.heappush(diff,x[i]-x[i+1]+1)
    temp=0
    for _ in range(n-1):
        temp-=heapq.heappop(diff)
    print(x[m-1]-x[0]+1-temp-n)