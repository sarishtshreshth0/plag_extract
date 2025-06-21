from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
q = deque([3,5,7])
res = 0
def chk(s):
    global res
    if min(s.count('3'), s.count('5'), s.count('7')) > 0:
        res += 1
while q:
    now = q.popleft()
    if now > n:
        continue
    chk(str(now))
    for t in ['3', '5', '7']:
        q.append(int(str(now) + t))
print(res)
