import heapq
n,m = map(int,input().split())
dp = [0]*(n+1)
L = []
days = []
cost = []
for i in range(n):
    a,b = map(int,input().split())
    if a > m:
        continue
    L.append([a,b])

L.sort(reverse = True)

ans = 0
li = []
for i in range(1,m+1):
    while L and L[-1][0] <= i:
        (a,b) = L.pop()
        heapq.heappush(li,b*(-1))

    if li:
        h = heapq.heappop(li)
        ans +=(-1)*h

print(ans)