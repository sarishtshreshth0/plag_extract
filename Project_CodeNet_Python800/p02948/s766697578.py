import sys
input = sys.stdin.buffer.readline

n, m = map(int, input().split())
AB = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append((a, b))
#AB.sort(key = lambda x:(-x[0], -x[1]))
AB.sort(reverse=True)
#print(AB)

h = []
import heapq
heapq.heapify(h)
ans = 0
for i in reversed(range(m)):
    while AB:
        a, b = AB.pop()
        if i+a > m:
            AB.append((a, b))
            break
        else:
            heapq.heappush(h, (-b, a))
    #print(i, h)
    if h:
        b, a = heapq.heappop(h)
        b = b*(-1)
        ans += b
print(ans)
