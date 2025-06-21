from collections import deque
n,m = map(int,input().split())
e = [[] for i in range(n)]
l = [-1]*n
for i in range(m):
    a,b,c = map(int,input().split())
    e[a-1].append(b-1)
    e[b-1].append(a-1)

def dfs(x,count):
    l[x] = count
    q = deque([])
    q.append(x)
    while q:
        bef = q.popleft()
        for nex in e[bef]:
            if l[nex] == -1:
                l[nex] = count
                q.append(nex)
count = 0
for i in range(n):
    if l[i] == -1 and e[i]:
        dfs(i,count)
        count += 1
print(count+l.count(-1))