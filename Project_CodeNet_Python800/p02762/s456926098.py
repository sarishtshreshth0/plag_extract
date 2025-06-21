import sys
sys.setrecursionlimit(2**20)
n, m, k = map(int, input().split())
ab = []
for _ in range(m):
    ab.append([int(x)-1 for x in input().split()])
cd = []
for _ in range(k):
    cd.append([int(x)-1 for x in input().split()])
group = [-1 for _ in range(n)]
lis = [[] for _ in range(n)]
for x in ab:
    a = x[0]
    b = x[1]
    lis[a].append(b)
    lis[b].append(a)
g_n = 0
def dfs(now):
    global g_n
    group[now] = g_n
    global group_len_n
    group_len_n += 1
    for i in lis[now]:
        if group[i] == -1:
            dfs(i)
group_len = []
for i in range(n):
    if group[i] == -1:
        group_len_n = 0
        dfs(i)
        group_len.append(group_len_n)
        g_n += 1
friend = [0 for _ in range(n)]
block = [0 for _ in range(n)]
for x in ab:
    a = x[0]
    b = x[1]
    if group[a] == group[b]:
        friend[a] += 1
        friend[b] += 1
for x in cd:
    c = x[0]
    d = x[1]
    if group[c] == group[d]:
        block[c] += 1
        block[d] += 1
ans = []
for i in range(n):
    ans.append(str(group_len[group[i]] - friend[i] - block[i] -1))
print(" ".join(ans))