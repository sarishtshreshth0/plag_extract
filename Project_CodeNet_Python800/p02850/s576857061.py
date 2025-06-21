import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
import bisect

INF = 10**9+7

if __name__ == "__main__":
    n = int(input())
    edge = [[] for i in range(n)]
    side = []
    for i in range(n-1):
        a,b = map(int,input().split())
        a-=1
        b-=1
        edge[a].append(b)
        edge[b].append(a)
        side.append([a,b])
    I = collections.defaultdict(lambda : 0)
    k = 0
    for i in edge:
        k = max(k,len(i))
    print(k)
    color = [INF]*(n)
    d = [INF]*(n)
    d[0] = 0
    q = collections.deque([0])
    while q:
        p = q.popleft()
        color_num = 1
        for v in edge[p]:
            if d[v] == INF:
                q.append(v)
                d[v] = d[p] + 1
                if color_num == color[p]:
                    color_num+=1
                color[v] = color_num
                I[(p,v)] = color_num
                I[(v,p)] = color_num
                color_num+=1
    for i,j in side:
        print(I[(i,j)])