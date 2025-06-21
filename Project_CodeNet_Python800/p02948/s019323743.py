from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
jobs = [inpl() for _ in range(n)]
jobs.sort()
can = []
ind = 0
res = 0
for i in range(1,m+1):
    while ind < n:
        a,b = jobs[ind]
        if a == i:
            heappush(can,-b)
            ind += 1
            continue
        break
    if can != []:
        res -= heappop(can)
print(res)