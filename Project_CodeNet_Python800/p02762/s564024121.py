import sys
sys.setrecursionlimit(10**7)
n , m , k = map(int, input().split())
r = [[] for i in range(n)]
bk = [[] for i in range(n)]
for i in range(m):
    a , b = map(int, input().split())
    r[a-1].append(b-1)
    r[b-1].append(a-1)
for i in range(k):
    c , d = map(int, input().split())
    bk[c-1].append(d-1)
    bk[d-1].append(c-1)


v=[0]*n
l=[0]*n
w=[0]*n

def dfs(now,c):
    global ln
    if v[now]==1:
        return
    v[now]=1
    ln+=1
    w[now]=c
    l[c]=ln
    for i in r[now]:
        dfs(i,c)
    return

for i in range(n):
    ln=0
    dfs(i,i)

ans =[]
for i in range(n):
    d=0
    for j in bk[i]:
        if w[j]==w[i]:
            d+=1
    ans.append(str(l[w[i]]-1-d-len(r[i])))
print(' '.join(ans))
