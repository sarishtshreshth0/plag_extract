from _collections import deque
n,m,k=map(int,input().split())
import sys
sys.setrecursionlimit(10**9) #再帰の上限をあげる

fre=[[] for _ in range(n+1)]
bro=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    fre[a].append(b)
    fre[b].append(a)

for i in range(k):
    a, b = map(int, input().split())
    bro[a].append(b)
    bro[b].append(a)

ans=[]

x=[-1]*(n+1)

def s(y):
    global i
    if x[y]>0:
        return
    x[y]=i
    for j in fre[y]:
        if x[j]==-1:
            s(j)

for i in range(1,n+1):
    s(i)

g=[0]*(n+1)
for i in range(1,n+1):
    g[x[i]]+=1
for i in range(1,n+1):
    g[i]=g[x[i]]

for i in range(1,n+1):
    aa=g[i]-1
    aa-=len(fre[i])
    for j in bro[i]:
        if x[i]==x[j]:
            aa-=1
    ans.append(str(aa))
print(" ".join(ans))

