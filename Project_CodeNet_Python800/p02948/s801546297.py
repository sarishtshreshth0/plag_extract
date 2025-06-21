 # AtCoder
import heapq
N, M = map(int, input().split())
AB = [[] for _ in range(M+1)]
for i in range(N):
    A, B = map(int, input().split())
    if M >= A:
        AB[A].append(B)

hp = []
ans = 0

for B in AB:
    for b in B:
        heapq.heappush(hp, (-1)*b)
    if hp:
        ans += heapq.heappop(hp)*(-1)
print(ans)
