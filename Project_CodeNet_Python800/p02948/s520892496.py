import heapq
n, m = map(int, input().split())
work = [0]*n
for i in range(n):
  work[i] = list(map(int, input().split()))

work.sort()
k = 0
workable = []
heapq.heapify(workable)
ans = 0
for i in range(m):
  while k < n:
    if work[k][0] <= i+1:
      heapq.heappush(workable, -work[k][1])
      k += 1
    else:
      break
  if workable:
    ans += -heapq.heappop(workable)
print(ans)