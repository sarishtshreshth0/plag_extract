import heapq

N, M = map(int, input().split())

# [0日後(今日), 1日後, ..., M-1日後]
jobs = [[] for _ in range(M)]
for i in range(N):
    a, b = map(int, input().split())
    if M - a >= 0:
        jobs[M - a].append(b)

ans = 0
q = []

# M-1日後にできる仕事, ..., 1日後, 0日後
# A >= 1なのでM日後にできる仕事はない

# heappop()で出てくるのは最小値
# 最大値が欲しい場合は-1倍してpush(), pop()して-1倍

# i = M-1, M-2, ..., 1, 0
for i in range(M - 1, -1, -1):
    for values in jobs[i]:
        heapq.heappush(q, -1 * values)
    if len(q) > 0:
        ans += heapq.heappop(q) * (-1)

print(ans)
