jobs, limit = map(int, input().split())
fees = [[] for _ in range(limit)]
for _ in range(jobs):
    day, fee = map(int, input().split())
    if day - 1 < limit:
        fees[day - 1] += [fee]
        
import heapq  # heapqライブラリのimport

res = 0
array = []
for fee_list in fees:
    [heapq.heappush(array, -f) for f in fee_list]
    if len(array) > 0:
        res += -heapq.heappop(array)
print(res)