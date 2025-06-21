import heapq

n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.append([m+1,0])
ab = sorted(ab, key=lambda x:x[0])



max_values = [0 for _ in range(m)]
hq = []

possible_days = 0

for now in range(n+1):
    # if necessary day exceed the (now_day), extract the most valuable work
    while possible_days <= ab[now][0]:
        if len(hq) < 1:
            pass
        else:
            max_values[possible_days-2] = -heapq.heappop(hq)
        possible_days += 1
    if possible_days-2 > m-1:
        break
    heapq.heappush(hq, -ab[now][1])
print(sum(max_values))