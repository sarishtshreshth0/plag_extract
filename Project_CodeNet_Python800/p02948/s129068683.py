# https://atcoder.jp/contests/abc137/tasks/abc137_d

# 最終日に選ぶことができるのは、Ai=1だけ
# 最終-1日に選ぶことができるのは、Ai=1,2だけ

from collections import defaultdict
from heapq import heapify, heappush, heappop

n, m = map(int, input().split())
d = defaultdict(list)
queue = []

for _ in range(n):
    a, b = map(int, input().split())
    d[a].append(b)

ans = 0
for i in range(1, m + 1):
    for j in d[i]:
        heappush(queue, -j) # j日目までを全部push
    if len(queue) > 0: # 取れたら最大を取ってきて足す
        ans += heappop(queue) * -1

print(ans)