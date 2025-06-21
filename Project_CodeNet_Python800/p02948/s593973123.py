import heapq
from collections import defaultdict

N, M = map(int, input().split())
salary = defaultdict(list)
for i in range(N):
    a, b = map(int, input().split())
    salary[a].append(-b)

sv = []
heapq.heapify(sv)
ans = 0
for i in range(1, M+1):
    for j in range(len(salary[i])):
        heapq.heappush(sv, salary[i][j])
    if(len(sv)):
        ans -= heapq.heappop(sv)
print(ans)