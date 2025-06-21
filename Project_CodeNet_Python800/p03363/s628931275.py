import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = [0]+list(mapint())
from itertools import accumulate
from collections import Counter

cAs = list(accumulate(As))
c = Counter(cAs)
ans = 0
for num, c in c.most_common():
    if c<2:
        break
    ans += c*(c-1)//2
print(ans)