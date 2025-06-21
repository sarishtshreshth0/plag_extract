import collections
import heapq
n,m = map(int,raw_input().split(' '))

elems = [map(int, raw_input().split(' ')) for _ in range(n)]
elems.sort(key = lambda x:x[0])
heap = []

j = 0
cumul = 0
for i in range(1,m+1):

	while(j < len(elems) and elems[j][0] <= i): 
		heapq.heappush(heap,-elems[j][1])
		j+=1
	if heap:
		cumul -= heapq.heappop(heap)

print cumul