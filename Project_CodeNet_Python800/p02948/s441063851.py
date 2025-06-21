import heapq
n,m=map(int, input().split())
lst = []
for i in range(n):
  a,b=map(int, input().split())
  lst.append((-b,a))
lst = sorted(lst, key=lambda x:x[1])

now_idx = 0
queue = []
sum_ = 0
for i in range(1,m+1):
  for j in range(now_idx, n):
    if lst[j][1] <= i:
      heapq.heappush(queue, lst[j])
    else:
      now_idx = j
      break
  else:
    now_idx = n
  if len(queue)>0:
    sum_ -= heapq.heappop(queue)[0]
print(sum_)
