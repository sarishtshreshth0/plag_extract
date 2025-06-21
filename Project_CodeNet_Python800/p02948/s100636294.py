# 参考　yy4さん
from heapq import heappush, heappop
import sys    
input = sys.stdin.readline    
n, m = map(int, input().split())
    
vmax = pow(10, 5)
jobs = {i:[] for i in range(1,vmax + 1)}
for _ in range(n):
    a, b = map(int, input().split())
    jobs[a].append(-b)
    

ans =0
hq = []
for i in range(1, m + 1):
    for j in jobs[i]:
        heappush(hq, j)
    if hq:
        v = heappop(hq)
        v *= -1
        ans += v
print(ans)