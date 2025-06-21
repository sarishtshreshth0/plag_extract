import heapq

dic = {}
n, m = map(int, input().split())
for _ in range(n):
  a, b = map(int, input().split())
  if dic.get(a) is not None:
    dic[a].append(-b)
  else:
    dic[a] = [-b,]

ans = 0
bite = []
for i in range(1, m+1):
  if dic.get(i) is not None:
    #bite = bite + dic[i]
    for val in dic[i]:
      heapq.heappush(bite, val)
  if len(bite) > 0:
    #heapq.heapify(bite)
    ans += heapq.heappop(bite)
print(ans*-1)