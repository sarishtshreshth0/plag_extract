import heapq

N, M = map(int, input().split())
ABs = [tuple(map(int, input().split())) for _ in range(N)]
ABs.sort(reverse = True)

works = []
reward = 0
for i in range(1, M+1):
	while ABs and ABs[-1][0] <= i:
		heapq.heappush(works, -ABs.pop()[1])
	if works:
		reward -= heapq.heappop(works)
        
print(reward)