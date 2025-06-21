from operator import itemgetter
import heapq

N, M = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(N)]
pairs.sort(key = itemgetter(0))

heap = []
reward = 0
index_of_pairs = 0   
for i in range(1, M+1):
    while index_of_pairs < N and pairs[index_of_pairs][0] <= i:
        heapq.heappush(heap, -pairs[index_of_pairs][1])
        index_of_pairs += 1
    if heap:
        reward -= heapq.heappop(heap)

print(reward)            
