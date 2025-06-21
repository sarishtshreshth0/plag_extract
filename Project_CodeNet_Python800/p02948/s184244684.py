import heapq
N, M = map(int, input().split())

jobs = [[] for _ in range(M + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    if a > M:
        continue # M日の期間を越えるような仕事は請けない
    jobs[a].append(-b)

heap = []
salary = 0

for day in range(1, M + 1):
  for i in jobs[day]:
    heapq.heappush(heap, i)

  if len(heap) > 0:
    salary += abs(heapq.heappop(heap)) # heappopは常に最小のもの(一番絶対値の大きい)を返す

print(salary)