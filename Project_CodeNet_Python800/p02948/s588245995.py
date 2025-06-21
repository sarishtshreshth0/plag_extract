from heapq import heappush, heappop
import sys

input = sys.stdin.buffer.readline
n, m = map(int, input().split())
AB = []
AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort(key=lambda x: [-x[0], -x[1]])
ans = 0
kouho = []
for d in range(1, m + 1):
    while AB and AB[-1][0] <= d:
        a, b = AB.pop()
        heappush(kouho, (-b, a))
    if kouho:
        p, q = heappop(kouho)
        ans += -p
print(ans)
