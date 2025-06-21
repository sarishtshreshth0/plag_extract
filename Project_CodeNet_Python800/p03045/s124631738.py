n,m=map(int,input().split())
par=[-1]*n
def find(x):
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def union(x,y):
    x,y=find(x),find(y)
    if x!=y:
        if x>y:
            x,y=y,x
        par[x]+=par[y]
        par[y]=x

for i in range(m):
    x,y,z=map(int,input().split())
    union(x-1,y-1)

ans=0
for i in range(n):
    if par[i]<0:
        ans+=1
        n+=par[i]
print(ans+n)