from heapq import heappush, heappop

n, m = [int(x) for x in input().split()]

temp_list = []
for _ in range(m + 1):
    temp_list.append([])
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    if a > m:
        continue
    temp_list[a].append(-b)

h = []
ans = 0
for i in range(1, m + 1):
    for b in temp_list[i]:
        heappush(h, b)

    if len(h) == 0:
        continue
    
    ans -= heappop(h)
print(ans)