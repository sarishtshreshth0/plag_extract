n=int(input())

a=[0]*n
b=[0]*n
c=[0]*n
d=[0]*n
edges=[set() for _ in range(n)]
matched=[-1]*n

for i in range(n):
    ta,tb=list(map(int,input().split()))
    a[i]=ta
    b[i]=tb

for i in range(n):
    tc,td=list(map(int,input().split()))
    c[i]=tc
    d[i]=td

for i in range(n):
    for j in range(n):
        if a[i]<c[j] and b[i]<d[j]:
            edges[i].add(j)

def dfs(v,visited):
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u]==-1 or dfs(matched[u],visited):
            matched[u]=v
            return True
    
    return False

print(sum(dfs(s,set()) for s in range(n)))