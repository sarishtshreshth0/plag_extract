import heapq

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
kouho = []
ans = 0

AB = sorted(AB)

# 後ろから見て優先度付きキューで取り出す
n = 0
heapq.heapify(kouho)
for i in range(1, M+1):
    if n < N:
        while AB[n][0] <= i:
            heapq.heappush(kouho, AB[n][1] * (-1))
            n += 1
            if n >= N:
                break
    
    if kouho:
        b = heapq.heappop(kouho)
        ans += b*(-1)
    
print(ans)