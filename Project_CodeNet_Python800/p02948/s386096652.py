import heapq

n, m = map(int, input().split())
num = sorted([list(map(int, input().split())) for i in range(n)], key = lambda x: x[0])

s = []
j = 0
count = 0
heapq.heapify(s)

for i in range(1, m + 1):
  while (j < n and num[j][0] <= i):
    heapq.heappush(s, num[j][1] * (-1))
    j += 1
  if(len(s)):
    count += heapq.heappop(s) * (-1)

print(count)
