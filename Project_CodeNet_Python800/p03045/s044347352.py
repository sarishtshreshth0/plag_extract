n,m=map(int,input().split())

import sys
sys.setrecursionlimit(10**9) #再帰の上限をあげる

root=[i for i in range(n+1)] #自分が親なら自身の番号を、そうでないなら（元）親の番号を示す

def r(x):   #親は誰？
    if root[x]==x:
        return x
    else:
        root[x]=r(root[x])
        return root[x]

def unite(x,y):
    x=r(x)
    y=r(y)
    if x==y:
        return
    if x>y:
        x,y=y,x
    root[y]=x

for i in range(m):
    x,y,z=map(int,input().split())
    unite(x,y)

ans=0
for i in range(1,n+1):
    if root[i]==i:
        ans+=1
print(ans)


