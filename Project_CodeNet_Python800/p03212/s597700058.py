import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy

ans = []
def dfs(a,m):
    global ans
    if len(a) == m:
        s = ""
        for i in range(m):
            s += str(a[i])
        if "7" in s and "5" in s and "3" in s:
            ans.append(int(s))
        return
    for i in [3,5,7]:
        a.append(i)
        dfs(a,m)
        a.pop()
if __name__ == "__main__":
    n = int(input())
    m = len(str(n))
    a = []
    for i in range(3,m+1):
        dfs(a,i)
    ans.sort()
    cnt = 0
    for i in range(len(ans)):
        if ans[i] <= n:
            cnt+=1
    print(cnt)
