import sys
import math
import numpy as np
import copy

def dfs(now, group, groups, edges):
    if groups[now] != -1:
        return 0
    groups[now] = group
    cnt = 1
    for to in edges[now]:
        cnt += dfs(to, group, groups, edges)
    return cnt

def main():
    n, m, k = map(int, input().split())
    edges = [list() for i in range(n)]
    ngs = [list() for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        edges[a].append(b)
        edges[b].append(a)
    for i in range(k):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        ngs[c].append(d)
        ngs[d].append(c)


    cnt = 0
    groups = [-1 for i in range(n)]
    nodes_cnt = list()

    ans = [0 for i in range(n)]
    
    for i in range(n):
        if groups[i] == -1:
            nodes_cnt.append(dfs(i, cnt, groups, edges))
            cnt += 1
        ans[i] = nodes_cnt[groups[i]] - len(edges[i]) - 1
        for ng in ngs[i]:
            if groups[i] == groups[ng]:
                ans[i] -= 1

    print(*ans, sep=" ")

if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    sys.exit(main())